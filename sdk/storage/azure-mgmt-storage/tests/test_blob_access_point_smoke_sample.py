# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------
import importlib
from pathlib import Path
from unittest.mock import Mock, create_autospec

import pytest

from azure.core.exceptions import HttpResponseError
from azure.mgmt.storage import StorageManagementClient, models
from azure.mgmt.storage.operations import BlobAccessPointConfigurationsOperations, BlobContainersOperations


@pytest.fixture(scope="session", autouse=True)
def add_sanitizers():
    """Override the service-test fixture: these tests use no proxy or network."""


@pytest.fixture(name="sample")
def sample_module(monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "samples"))
    return importlib.import_module("blob_access_point_smoke_test")


@pytest.fixture(name="configuration")
def sample_configuration(sample):
    return sample.build_configuration(
        location="eastus",
        endpoint="https://s3.example.com/bucket",
        access_key_id="test-key",
        secret_access_key="test-secret",
        signing_region="us-east-1",
    )


@pytest.fixture(name="client")
def mocked_client():
    client = Mock(spec=StorageManagementClient)
    client.blob_access_point_configurations = create_autospec(BlobAccessPointConfigurationsOperations, instance=True)
    client.blob_containers = create_autospec(BlobContainersOperations, instance=True)
    operations = client.blob_access_point_configurations
    operations.begin_create.return_value.result.return_value = models.BlobAccessPointConfiguration(
        {"properties": {"uniqueId": "configuration-id"}}
    )
    operations.begin_test_existing_connection.return_value.result.return_value = (
        models.BlobAccessPointConnectionTestResponse(method_name="ListObjectsV2", request_id="request-id")
    )
    operations.get.return_value = models.BlobAccessPointConfiguration(
        {"properties": {"lastConnectionTestStatus": "Succeeded"}}
    )
    client.blob_containers.get.return_value = models.BlobContainer(
        container_properties=models.ContainerProperties(
            blob_access_point_configuration=models.BlobAccessPointConfigurationConnection(
                blob_access_point_configuration_name="smoke-config",
                blob_access_point_configuration_unique_id="configuration-id",
            )
        )
    )
    return client


def execute(sample, client, configuration):
    return sample.run_smoke_test(
        client,
        resource_group_name="test-group",
        account_name="testaccount",
        configuration_name="smoke-config",
        container_name="smoke-container",
        configuration=configuration,
    )


def test_configuration_wire_payload(configuration):
    assert configuration.as_dict(exclude_readonly=True) == {
        "location": "eastus",
        "properties": {
            "description": "S3-compatible source smoke test",
            "state": "Active",
            "source": {
                "sourceType": "S3Compatible",
                "connection": {
                    "connectionType": "Endpoint",
                    "endpoint": "https://s3.example.com/bucket",
                    "tlsVerification": "Perform",
                },
                "auth": {
                    "authType": "AccessKey",
                    "accessKeyId": "test-key",
                    "secretAccessKey": "test-secret",
                    "signingRegion": "us-east-1",
                },
            },
        },
    }


def test_default_mode_is_offline(sample, monkeypatch, capsys):
    monkeypatch.setenv("S3_SECRET_ACCESS_KEY", "must-not-appear")
    constructor = Mock(side_effect=AssertionError("Offline mode must not construct an ARM client"))
    monkeypatch.setattr(sample, "StorageManagementClient", constructor)
    sample.main([])
    output = capsys.readouterr().out
    assert "OFFLINE" in output
    assert "must-not-appear" not in output
    assert "<redacted>" in output
    constructor.assert_not_called()


def test_execute_requires_inputs_before_constructing_client(sample, monkeypatch, capsys):
    monkeypatch.delenv("S3_ENDPOINT", raising=False)
    constructor = Mock()
    monkeypatch.setattr(sample, "StorageManagementClient", constructor)
    with pytest.raises(SystemExit) as error:
        sample.main(["--execute"])
    assert error.value.code == 2
    assert "S3_ENDPOINT" in capsys.readouterr().err
    constructor.assert_not_called()


def test_success_tests_and_binds_same_configuration(sample, client, configuration):
    assert execute(sample, client, configuration) is client.blob_containers.get.return_value
    request = client.blob_access_point_configurations.begin_test_existing_connection.call_args.kwargs["body"]
    assert request.unique_id == "configuration-id"
    container = client.blob_containers.create.call_args.kwargs["blob_container"]
    binding = container.container_properties.blob_access_point_configuration
    assert binding.blob_access_point_configuration_name == "smoke-config"
    assert binding.blob_access_point_configuration_unique_id == request.unique_id


def test_missing_unique_id_stops_before_connection_test(sample, client, configuration):
    client.blob_access_point_configurations.begin_create.return_value.result.return_value = (
        models.BlobAccessPointConfiguration({"properties": {}})
    )
    with pytest.raises(RuntimeError, match="no unique ID"):
        execute(sample, client, configuration)
    client.blob_access_point_configurations.begin_test_existing_connection.assert_not_called()
    client.blob_containers.create.assert_not_called()


@pytest.mark.parametrize("failure", ["response-error", "Failed", None, "http-error"])
def test_connection_failure_prevents_binding(sample, client, configuration, failure):
    operations = client.blob_access_point_configurations
    if failure == "response-error":
        operations.begin_test_existing_connection.return_value.result.return_value.error_message = "Access denied"
    elif failure == "http-error":
        operations.begin_test_existing_connection.return_value.result.side_effect = HttpResponseError(
            message="Access denied"
        )
    else:
        operations.get.return_value = models.BlobAccessPointConfiguration(
            {"properties": {"lastConnectionTestStatus": failure}}
        )
    with pytest.raises((RuntimeError, HttpResponseError)):
        execute(sample, client, configuration)
    client.blob_containers.create.assert_not_called()


@pytest.mark.parametrize("binding", [None, "wrong-name", "wrong-id"])
def test_binding_read_back_must_match(sample, client, configuration, binding):
    properties = client.blob_containers.get.return_value.container_properties
    if binding is None:
        properties.blob_access_point_configuration = None
    elif binding == "wrong-name":
        properties.blob_access_point_configuration.blob_access_point_configuration_name = "another-config"
    else:
        properties.blob_access_point_configuration.blob_access_point_configuration_unique_id = "another-id"
    with pytest.raises(RuntimeError, match="read-back"):
        execute(sample, client, configuration)
