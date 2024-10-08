# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.billing import BillingManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBillingManagementTransfersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(BillingManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.transfers.get(
            billing_account_name="str",
            billing_profile_name="str",
            invoice_section_name="str",
            transfer_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_initiate(self, resource_group):
        response = self.client.transfers.initiate(
            billing_account_name="str",
            billing_profile_name="str",
            invoice_section_name="str",
            transfer_name="str",
            parameters={"recipientEmailId": "str"},
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_cancel(self, resource_group):
        response = self.client.transfers.cancel(
            billing_account_name="str",
            billing_profile_name="str",
            invoice_section_name="str",
            transfer_name="str",
            api_version="2024-04-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list(self, resource_group):
        response = self.client.transfers.list(
            billing_account_name="str",
            billing_profile_name="str",
            invoice_section_name="str",
            api_version="2024-04-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
