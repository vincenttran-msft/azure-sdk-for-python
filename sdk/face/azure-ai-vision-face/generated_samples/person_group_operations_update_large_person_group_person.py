# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.ai.vision.face import FaceAdministrationClient

"""
# PREREQUISITES
    pip install azure-ai-vision-face
# USAGE
    python person_group_operations_update_large_person_group_person.py
"""


def main():
    client = FaceAdministrationClient(
        endpoint="ENDPOINT",
        credential="CREDENTIAL",
    )

    client.large_person_group.update_person(
        large_person_group_id="your_large_person_group_id",
        person_id="25985303-c537-4467-b41d-bdb45cd95ca1",
        body={"name": "your_large_person_group_person_name", "userData": "your_user_data"},
    )


# x-ms-original-file: v1.2-preview.1/PersonGroupOperations_UpdateLargePersonGroupPerson.json
if __name__ == "__main__":
    main()
