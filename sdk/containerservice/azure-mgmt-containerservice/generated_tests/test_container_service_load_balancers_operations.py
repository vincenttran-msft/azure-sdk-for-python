# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerservice import ContainerServiceClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerServiceLoadBalancersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerServiceClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_managed_cluster(self, resource_group):
        response = self.client.load_balancers.list_by_managed_cluster(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2024-03-02-preview",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.load_balancers.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            load_balancer_name="str",
            api_version="2024-03-02-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_create_or_update(self, resource_group):
        response = self.client.load_balancers.create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            load_balancer_name="str",
            api_version="2024-03-02-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.load_balancers.begin_delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            load_balancer_name="str",
            api_version="2024-03-02-preview",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
