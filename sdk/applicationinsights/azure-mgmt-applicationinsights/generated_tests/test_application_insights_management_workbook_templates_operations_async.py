# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.applicationinsights.aio import ApplicationInsightsManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApplicationInsightsManagementWorkbookTemplatesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApplicationInsightsManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workbook_templates_list_by_resource_group(self, resource_group):
        response = self.client.workbook_templates.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2020-11-20",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workbook_templates_get(self, resource_group):
        response = await self.client.workbook_templates.get(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-11-20",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workbook_templates_delete(self, resource_group):
        response = await self.client.workbook_templates.delete(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-11-20",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workbook_templates_create_or_update(self, resource_group):
        response = await self.client.workbook_templates.create_or_update(
            resource_group_name=resource_group.name,
            resource_name="str",
            workbook_template_properties={
                "location": "str",
                "author": "str",
                "galleries": [{"category": "str", "name": "str", "order": 0, "resourceType": "str", "type": "str"}],
                "id": "str",
                "localized": {
                    "str": [
                        {
                            "galleries": [
                                {"category": "str", "name": "str", "order": 0, "resourceType": "str", "type": "str"}
                            ],
                            "templateData": {},
                        }
                    ]
                },
                "name": "str",
                "priority": 0,
                "tags": {"str": "str"},
                "templateData": {},
                "type": "str",
            },
            api_version="2020-11-20",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_workbook_templates_update(self, resource_group):
        response = await self.client.workbook_templates.update(
            resource_group_name=resource_group.name,
            resource_name="str",
            api_version="2020-11-20",
        )

        # please add some check logic here by yourself
        # ...
