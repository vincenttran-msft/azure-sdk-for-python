# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionsRequired(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Any action that is required beyond basic workflow (approve/ reject/ disconnect)."""

    NONE = "None"
    RECREATE = "Recreate"


class ConfigurationResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The resource type to check for name availability."""

    MICROSOFT_APP_CONFIGURATION_CONFIGURATION_STORES = "Microsoft.AppConfiguration/configurationStores"


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private link service connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the configuration store need to be recovered."""

    RECOVER = "Recover"
    DEFAULT = "Default"


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an
    implicitly created identity and a set of user-assigned identities. The type 'None' will remove
    any identities.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the configuration store."""

    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Control permission for data plane traffic coming from public networks while private endpoint is
    enabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ReplicaProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the replica."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    CANCELED = "Canceled"