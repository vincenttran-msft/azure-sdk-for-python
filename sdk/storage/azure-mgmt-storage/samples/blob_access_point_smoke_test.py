# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------
"""Preview the request offline, or explicitly execute the management-plane smoke test."""

import argparse
import json
import os
from collections.abc import Sequence

from azure.mgmt.storage import StorageManagementClient, models


def build_configuration(
    *,
    location: str,
    endpoint: str,
    access_key_id: str,
    secret_access_key: str,
    signing_region: str,
) -> models.BlobAccessPointConfiguration:
    return models.BlobAccessPointConfiguration(
        location=location,
        properties=models.BlobAccessPointConfigurationProperties(
            description="S3-compatible source smoke test",
            state=models.BlobAccessPointConfigurationState.ACTIVE,
            source=models.BlobAccessPointGenericS3SourceProperties(
                connection=models.BlobAccessPointEndpointConnectionProperties(
                    endpoint=endpoint,
                    tls_verification=models.BlobAccessPointTlsVerification.PERFORM,
                ),
                auth=models.BlobAccessPointAccessKeyAuthProperties(
                    access_key_id=access_key_id,
                    secret_access_key=secret_access_key,
                    signing_region=signing_region,
                ),
            ),
        ),
    )


def run_smoke_test(
    client: StorageManagementClient,
    *,
    resource_group_name: str,
    account_name: str,
    configuration_name: str,
    container_name: str,
    configuration: models.BlobAccessPointConfiguration,
) -> models.BlobContainer:
    operations = client.blob_access_point_configurations
    target = {
        "resource_group_name": resource_group_name,
        "account_name": account_name,
        "blob_access_point_configuration_name": configuration_name,
    }
    created = operations.begin_create(**target, resource=configuration).result()
    unique_id = created.properties.unique_id
    if not unique_id:
        raise RuntimeError("Configuration creation returned no unique ID; container was not bound.")

    result = operations.begin_test_existing_connection(
        **target,
        body=models.BlobAccessPointConnectionTestRequest(unique_id=unique_id),
    ).result()
    if result.error_message:
        raise RuntimeError(f"Connection test failed: {result.error_message}")

    properties = operations.get(**target).properties
    if properties.last_connection_test_status != models.BlobAccessPointConnectionTestStatus.SUCCEEDED:
        raise RuntimeError(
            f"Connection test was not confirmed successful: {properties.last_connection_test_status}; "
            f"{properties.last_connection_test_error_message}"
        )

    containers = client.blob_containers
    container_target = {
        "resource_group_name": resource_group_name,
        "account_name": account_name,
        "container_name": container_name,
    }
    containers.create(
        **container_target,
        blob_container=models.BlobContainer(
            container_properties=models.ContainerProperties(
                blob_access_point_configuration=models.BlobAccessPointConfigurationConnection(
                    blob_access_point_configuration_name=configuration_name,
                    blob_access_point_configuration_unique_id=unique_id,
                )
            )
        ),
    )
    container = containers.get(**container_target)
    binding = container.container_properties.blob_access_point_configuration if container.container_properties else None
    if (
        not binding
        or binding.blob_access_point_configuration_name != configuration_name
        or binding.blob_access_point_configuration_unique_id != unique_id
    ):
        raise RuntimeError("Container read-back did not confirm the requested configuration binding.")
    return container


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Make Azure requests and create resources. Without this flag, use synthetic inputs offline.",
    )
    args = parser.parse_args(argv)
    if not args.execute:
        configuration = build_configuration(
            location="eastus",
            endpoint="https://s3.example.com/smoke-test-bucket",
            access_key_id="offline-placeholder",
            secret_access_key="offline-placeholder",
            signing_region="us-east-1",
        )
        payload = configuration.as_dict(exclude_readonly=True)
        payload["properties"]["source"]["auth"]["accessKeyId"] = "<redacted>"
        payload["properties"]["source"]["auth"]["secretAccessKey"] = "<redacted>"
        print("OFFLINE: synthetic inputs only; no credentials loaded and no requests sent.")
        print(json.dumps(payload, indent=2))
        return

    required = (
        "AZURE_SUBSCRIPTION_ID",
        "AZURE_RESOURCE_GROUP",
        "AZURE_STORAGE_ACCOUNT",
        "AZURE_LOCATION",
        "BLOB_ACCESS_POINT_CONFIGURATION_NAME",
        "BLOB_ACCESS_POINT_CONTAINER_NAME",
        "S3_ENDPOINT",
        "S3_ACCESS_KEY_ID",
        "S3_SECRET_ACCESS_KEY",
        "S3_SIGNING_REGION",
    )
    missing = [name for name in required if not os.environ.get(name)]
    if missing:
        parser.error(f"Missing required environment variables: {', '.join(missing)}")

    from azure.identity import DefaultAzureCredential  # pylint: disable=import-outside-toplevel

    configuration = build_configuration(
        location=os.environ["AZURE_LOCATION"],
        endpoint=os.environ["S3_ENDPOINT"],
        access_key_id=os.environ["S3_ACCESS_KEY_ID"],
        secret_access_key=os.environ["S3_SECRET_ACCESS_KEY"],
        signing_region=os.environ["S3_SIGNING_REGION"],
    )
    with (
        DefaultAzureCredential() as credential,
        StorageManagementClient(
            credential=credential,
            subscription_id=os.environ["AZURE_SUBSCRIPTION_ID"],
            api_version="2026-09-01",
        ) as client,
    ):
        run_smoke_test(
            client,
            resource_group_name=os.environ["AZURE_RESOURCE_GROUP"],
            account_name=os.environ["AZURE_STORAGE_ACCOUNT"],
            configuration_name=os.environ["BLOB_ACCESS_POINT_CONFIGURATION_NAME"],
            container_name=os.environ["BLOB_ACCESS_POINT_CONTAINER_NAME"],
            configuration=configuration,
        )
    print("Connection test and container binding read-back succeeded. Blob reads have not been tested.")


if __name__ == "__main__":
    main()
