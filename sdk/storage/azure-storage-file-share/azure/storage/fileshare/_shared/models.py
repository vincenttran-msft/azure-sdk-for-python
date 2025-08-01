# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# pylint: disable=too-many-instance-attributes
from enum import Enum
from typing import Optional

from azure.core import CaseInsensitiveEnumMeta
from azure.core.configuration import Configuration
from azure.core.pipeline.policies import UserAgentPolicy


def get_enum_value(value):
    if value is None or value in ["None", ""]:
        return None
    try:
        return value.value
    except AttributeError:
        return value


class StorageErrorCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Error codes returned by the service."""

    # Generic storage values
    ACCOUNT_ALREADY_EXISTS = "AccountAlreadyExists"
    ACCOUNT_BEING_CREATED = "AccountBeingCreated"
    ACCOUNT_IS_DISABLED = "AccountIsDisabled"
    AUTHENTICATION_FAILED = "AuthenticationFailed"
    AUTHORIZATION_FAILURE = "AuthorizationFailure"
    NO_AUTHENTICATION_INFORMATION = "NoAuthenticationInformation"
    CONDITION_HEADERS_NOT_SUPPORTED = "ConditionHeadersNotSupported"
    CONDITION_NOT_MET = "ConditionNotMet"
    EMPTY_METADATA_KEY = "EmptyMetadataKey"
    INSUFFICIENT_ACCOUNT_PERMISSIONS = "InsufficientAccountPermissions"
    INTERNAL_ERROR = "InternalError"
    INVALID_AUTHENTICATION_INFO = "InvalidAuthenticationInfo"
    INVALID_HEADER_VALUE = "InvalidHeaderValue"
    INVALID_HTTP_VERB = "InvalidHttpVerb"
    INVALID_INPUT = "InvalidInput"
    INVALID_MD5 = "InvalidMd5"
    INVALID_METADATA = "InvalidMetadata"
    INVALID_QUERY_PARAMETER_VALUE = "InvalidQueryParameterValue"
    INVALID_RANGE = "InvalidRange"
    INVALID_RESOURCE_NAME = "InvalidResourceName"
    INVALID_URI = "InvalidUri"
    INVALID_XML_DOCUMENT = "InvalidXmlDocument"
    INVALID_XML_NODE_VALUE = "InvalidXmlNodeValue"
    MD5_MISMATCH = "Md5Mismatch"
    METADATA_TOO_LARGE = "MetadataTooLarge"
    MISSING_CONTENT_LENGTH_HEADER = "MissingContentLengthHeader"
    MISSING_REQUIRED_QUERY_PARAMETER = "MissingRequiredQueryParameter"
    MISSING_REQUIRED_HEADER = "MissingRequiredHeader"
    MISSING_REQUIRED_XML_NODE = "MissingRequiredXmlNode"
    MULTIPLE_CONDITION_HEADERS_NOT_SUPPORTED = "MultipleConditionHeadersNotSupported"
    OPERATION_TIMED_OUT = "OperationTimedOut"
    OUT_OF_RANGE_INPUT = "OutOfRangeInput"
    OUT_OF_RANGE_QUERY_PARAMETER_VALUE = "OutOfRangeQueryParameterValue"
    REQUEST_BODY_TOO_LARGE = "RequestBodyTooLarge"
    RESOURCE_TYPE_MISMATCH = "ResourceTypeMismatch"
    REQUEST_URL_FAILED_TO_PARSE = "RequestUrlFailedToParse"
    RESOURCE_ALREADY_EXISTS = "ResourceAlreadyExists"
    RESOURCE_NOT_FOUND = "ResourceNotFound"
    SERVER_BUSY = "ServerBusy"
    UNSUPPORTED_HEADER = "UnsupportedHeader"
    UNSUPPORTED_XML_NODE = "UnsupportedXmlNode"
    UNSUPPORTED_QUERY_PARAMETER = "UnsupportedQueryParameter"
    UNSUPPORTED_HTTP_VERB = "UnsupportedHttpVerb"

    # Blob values
    APPEND_POSITION_CONDITION_NOT_MET = "AppendPositionConditionNotMet"
    BLOB_ACCESS_TIER_NOT_SUPPORTED_FOR_ACCOUNT_TYPE = "BlobAccessTierNotSupportedForAccountType"
    BLOB_ALREADY_EXISTS = "BlobAlreadyExists"
    BLOB_NOT_FOUND = "BlobNotFound"
    BLOB_OVERWRITTEN = "BlobOverwritten"
    BLOB_TIER_INADEQUATE_FOR_CONTENT_LENGTH = "BlobTierInadequateForContentLength"
    BLOCK_COUNT_EXCEEDS_LIMIT = "BlockCountExceedsLimit"
    BLOCK_LIST_TOO_LONG = "BlockListTooLong"
    CANNOT_CHANGE_TO_LOWER_TIER = "CannotChangeToLowerTier"
    CANNOT_VERIFY_COPY_SOURCE = "CannotVerifyCopySource"
    CONTAINER_ALREADY_EXISTS = "ContainerAlreadyExists"
    CONTAINER_BEING_DELETED = "ContainerBeingDeleted"
    CONTAINER_DISABLED = "ContainerDisabled"
    CONTAINER_NOT_FOUND = "ContainerNotFound"
    CONTENT_LENGTH_LARGER_THAN_TIER_LIMIT = "ContentLengthLargerThanTierLimit"
    COPY_ACROSS_ACCOUNTS_NOT_SUPPORTED = "CopyAcrossAccountsNotSupported"
    COPY_ID_MISMATCH = "CopyIdMismatch"
    FEATURE_VERSION_MISMATCH = "FeatureVersionMismatch"
    INCREMENTAL_COPY_BLOB_MISMATCH = "IncrementalCopyBlobMismatch"
    INCREMENTAL_COPY_OF_EARLIER_VERSION_SNAPSHOT_NOT_ALLOWED = "IncrementalCopyOfEarlierVersionSnapshotNotAllowed"
    #: Deprecated: Please use INCREMENTAL_COPY_OF_EARLIER_VERSION_SNAPSHOT_NOT_ALLOWED instead.
    INCREMENTAL_COPY_OF_ERALIER_VERSION_SNAPSHOT_NOT_ALLOWED = "IncrementalCopyOfEarlierVersionSnapshotNotAllowed"
    INCREMENTAL_COPY_SOURCE_MUST_BE_SNAPSHOT = "IncrementalCopySourceMustBeSnapshot"
    INFINITE_LEASE_DURATION_REQUIRED = "InfiniteLeaseDurationRequired"
    INVALID_BLOB_OR_BLOCK = "InvalidBlobOrBlock"
    INVALID_BLOB_TIER = "InvalidBlobTier"
    INVALID_BLOB_TYPE = "InvalidBlobType"
    INVALID_BLOCK_ID = "InvalidBlockId"
    INVALID_BLOCK_LIST = "InvalidBlockList"
    INVALID_OPERATION = "InvalidOperation"
    INVALID_PAGE_RANGE = "InvalidPageRange"
    INVALID_SOURCE_BLOB_TYPE = "InvalidSourceBlobType"
    INVALID_SOURCE_BLOB_URL = "InvalidSourceBlobUrl"
    INVALID_VERSION_FOR_PAGE_BLOB_OPERATION = "InvalidVersionForPageBlobOperation"
    LEASE_ALREADY_PRESENT = "LeaseAlreadyPresent"
    LEASE_ALREADY_BROKEN = "LeaseAlreadyBroken"
    LEASE_ID_MISMATCH_WITH_BLOB_OPERATION = "LeaseIdMismatchWithBlobOperation"
    LEASE_ID_MISMATCH_WITH_CONTAINER_OPERATION = "LeaseIdMismatchWithContainerOperation"
    LEASE_ID_MISMATCH_WITH_LEASE_OPERATION = "LeaseIdMismatchWithLeaseOperation"
    LEASE_ID_MISSING = "LeaseIdMissing"
    LEASE_IS_BREAKING_AND_CANNOT_BE_ACQUIRED = "LeaseIsBreakingAndCannotBeAcquired"
    LEASE_IS_BREAKING_AND_CANNOT_BE_CHANGED = "LeaseIsBreakingAndCannotBeChanged"
    LEASE_IS_BROKEN_AND_CANNOT_BE_RENEWED = "LeaseIsBrokenAndCannotBeRenewed"
    LEASE_LOST = "LeaseLost"
    LEASE_NOT_PRESENT_WITH_BLOB_OPERATION = "LeaseNotPresentWithBlobOperation"
    LEASE_NOT_PRESENT_WITH_CONTAINER_OPERATION = "LeaseNotPresentWithContainerOperation"
    LEASE_NOT_PRESENT_WITH_LEASE_OPERATION = "LeaseNotPresentWithLeaseOperation"
    MAX_BLOB_SIZE_CONDITION_NOT_MET = "MaxBlobSizeConditionNotMet"
    NO_PENDING_COPY_OPERATION = "NoPendingCopyOperation"
    OPERATION_NOT_ALLOWED_ON_INCREMENTAL_COPY_BLOB = "OperationNotAllowedOnIncrementalCopyBlob"
    PENDING_COPY_OPERATION = "PendingCopyOperation"
    PREVIOUS_SNAPSHOT_CANNOT_BE_NEWER = "PreviousSnapshotCannotBeNewer"
    PREVIOUS_SNAPSHOT_NOT_FOUND = "PreviousSnapshotNotFound"
    PREVIOUS_SNAPSHOT_OPERATION_NOT_SUPPORTED = "PreviousSnapshotOperationNotSupported"
    SEQUENCE_NUMBER_CONDITION_NOT_MET = "SequenceNumberConditionNotMet"
    SEQUENCE_NUMBER_INCREMENT_TOO_LARGE = "SequenceNumberIncrementTooLarge"
    SNAPSHOT_COUNT_EXCEEDED = "SnapshotCountExceeded"
    SNAPSHOT_OPERATION_RATE_EXCEEDED = "SnapshotOperationRateExceeded"
    #: Deprecated: Please use SNAPSHOT_OPERATION_RATE_EXCEEDED instead.
    SNAPHOT_OPERATION_RATE_EXCEEDED = "SnapshotOperationRateExceeded"
    SNAPSHOTS_PRESENT = "SnapshotsPresent"
    SOURCE_CONDITION_NOT_MET = "SourceConditionNotMet"
    SYSTEM_IN_USE = "SystemInUse"
    TARGET_CONDITION_NOT_MET = "TargetConditionNotMet"
    UNAUTHORIZED_BLOB_OVERWRITE = "UnauthorizedBlobOverwrite"
    BLOB_BEING_REHYDRATED = "BlobBeingRehydrated"
    BLOB_ARCHIVED = "BlobArchived"
    BLOB_NOT_ARCHIVED = "BlobNotArchived"

    # Queue values
    INVALID_MARKER = "InvalidMarker"
    MESSAGE_NOT_FOUND = "MessageNotFound"
    MESSAGE_TOO_LARGE = "MessageTooLarge"
    POP_RECEIPT_MISMATCH = "PopReceiptMismatch"
    QUEUE_ALREADY_EXISTS = "QueueAlreadyExists"
    QUEUE_BEING_DELETED = "QueueBeingDeleted"
    QUEUE_DISABLED = "QueueDisabled"
    QUEUE_NOT_EMPTY = "QueueNotEmpty"
    QUEUE_NOT_FOUND = "QueueNotFound"

    # File values
    CANNOT_DELETE_FILE_OR_DIRECTORY = "CannotDeleteFileOrDirectory"
    CLIENT_CACHE_FLUSH_DELAY = "ClientCacheFlushDelay"
    DELETE_PENDING = "DeletePending"
    DIRECTORY_NOT_EMPTY = "DirectoryNotEmpty"
    FILE_LOCK_CONFLICT = "FileLockConflict"
    FILE_SHARE_PROVISIONED_BANDWIDTH_DOWNGRADE_NOT_ALLOWED = "FileShareProvisionedBandwidthDowngradeNotAllowed"
    FILE_SHARE_PROVISIONED_IOPS_DOWNGRADE_NOT_ALLOWED = "FileShareProvisionedIopsDowngradeNotAllowed"
    INVALID_FILE_OR_DIRECTORY_PATH_NAME = "InvalidFileOrDirectoryPathName"
    PARENT_NOT_FOUND = "ParentNotFound"
    READ_ONLY_ATTRIBUTE = "ReadOnlyAttribute"
    SHARE_ALREADY_EXISTS = "ShareAlreadyExists"
    SHARE_BEING_DELETED = "ShareBeingDeleted"
    SHARE_DISABLED = "ShareDisabled"
    SHARE_NOT_FOUND = "ShareNotFound"
    SHARING_VIOLATION = "SharingViolation"
    SHARE_SNAPSHOT_IN_PROGRESS = "ShareSnapshotInProgress"
    SHARE_SNAPSHOT_COUNT_EXCEEDED = "ShareSnapshotCountExceeded"
    SHARE_SNAPSHOT_NOT_FOUND = "ShareSnapshotNotFound"
    SHARE_SNAPSHOT_OPERATION_NOT_SUPPORTED = "ShareSnapshotOperationNotSupported"
    SHARE_HAS_SNAPSHOTS = "ShareHasSnapshots"
    CONTAINER_QUOTA_DOWNGRADE_NOT_ALLOWED = "ContainerQuotaDowngradeNotAllowed"

    # DataLake values
    CONTENT_LENGTH_MUST_BE_ZERO = "ContentLengthMustBeZero"
    PATH_ALREADY_EXISTS = "PathAlreadyExists"
    INVALID_FLUSH_POSITION = "InvalidFlushPosition"
    INVALID_PROPERTY_NAME = "InvalidPropertyName"
    INVALID_SOURCE_URI = "InvalidSourceUri"
    UNSUPPORTED_REST_VERSION = "UnsupportedRestVersion"
    FILE_SYSTEM_NOT_FOUND = "FilesystemNotFound"
    PATH_NOT_FOUND = "PathNotFound"
    RENAME_DESTINATION_PARENT_PATH_NOT_FOUND = "RenameDestinationParentPathNotFound"
    SOURCE_PATH_NOT_FOUND = "SourcePathNotFound"
    DESTINATION_PATH_IS_BEING_DELETED = "DestinationPathIsBeingDeleted"
    FILE_SYSTEM_ALREADY_EXISTS = "FilesystemAlreadyExists"
    FILE_SYSTEM_BEING_DELETED = "FilesystemBeingDeleted"
    INVALID_DESTINATION_PATH = "InvalidDestinationPath"
    INVALID_RENAME_SOURCE_PATH = "InvalidRenameSourcePath"
    INVALID_SOURCE_OR_DESTINATION_RESOURCE_TYPE = "InvalidSourceOrDestinationResourceType"
    LEASE_IS_ALREADY_BROKEN = "LeaseIsAlreadyBroken"
    LEASE_NAME_MISMATCH = "LeaseNameMismatch"
    PATH_CONFLICT = "PathConflict"
    SOURCE_PATH_IS_BEING_DELETED = "SourcePathIsBeingDeleted"


class DictMixin(object):

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.keys())

    def __delitem__(self, key):
        self.__dict__[key] = None

    # Compare objects by comparing all attributes.
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    # Compare objects by comparing all attributes.
    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return str({k: v for k, v in self.__dict__.items() if not k.startswith("_")})

    def __contains__(self, key):
        return key in self.__dict__

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return [k for k in self.__dict__ if not k.startswith("_")]

    def values(self):
        return [v for k, v in self.__dict__.items() if not k.startswith("_")]

    def items(self):
        return [(k, v) for k, v in self.__dict__.items() if not k.startswith("_")]

    def get(self, key, default=None):
        if key in self.__dict__:
            return self.__dict__[key]
        return default


class LocationMode(object):
    """
    Specifies the location the request should be sent to. This mode only applies
    for RA-GRS accounts which allow secondary read access. All other account types
    must use PRIMARY.
    """

    PRIMARY = "primary"  #: Requests should be sent to the primary location.
    SECONDARY = "secondary"  #: Requests should be sent to the secondary location, if possible.


class ResourceTypes(object):
    """
    Specifies the resource types that are accessible with the account SAS.

    :param bool service:
        Access to service-level APIs (e.g., Get/Set Service Properties,
        Get Service Stats, List Containers/Queues/Shares)
    :param bool container:
        Access to container-level APIs (e.g., Create/Delete Container,
        Create/Delete Queue, Create/Delete Share,
        List Blobs/Files and Directories)
    :param bool object:
        Access to object-level APIs for blobs, queue messages, and
        files(e.g. Put Blob, Query Entity, Get Messages, Create File, etc.)
    """

    service: bool = False
    container: bool = False
    object: bool = False
    _str: str

    def __init__(
        self, service: bool = False, container: bool = False, object: bool = False  # pylint: disable=redefined-builtin
    ) -> None:
        self.service = service
        self.container = container
        self.object = object
        self._str = ("s" if self.service else "") + ("c" if self.container else "") + ("o" if self.object else "")

    def __str__(self):
        return self._str

    @classmethod
    def from_string(cls, string):
        """Create a ResourceTypes from a string.

        To specify service, container, or object you need only to
        include the first letter of the word in the string. E.g. service and container,
        you would provide a string "sc".

        :param str string: Specify service, container, or object in
            in the string with the first letter of the word.
        :return: A ResourceTypes object
        :rtype: ~azure.storage.fileshare.ResourceTypes
        """
        res_service = "s" in string
        res_container = "c" in string
        res_object = "o" in string

        parsed = cls(res_service, res_container, res_object)
        parsed._str = string
        return parsed


class AccountSasPermissions(object):
    """
    :class:`~ResourceTypes` class to be used with generate_account_sas
    function and for the AccessPolicies used with set_*_acl. There are two types of
    SAS which may be used to grant resource access. One is to grant access to a
    specific resource (resource-specific). Another is to grant access to the
    entire service for a specific account and allow certain operations based on
    perms found here.

    :param bool read:
        Valid for all signed resources types (Service, Container, and Object).
        Permits read permissions to the specified resource type.
    :param bool write:
        Valid for all signed resources types (Service, Container, and Object).
        Permits write permissions to the specified resource type.
    :param bool delete:
        Valid for Container and Object resource types, except for queue messages.
    :param bool delete_previous_version:
        Delete the previous blob version for the versioning enabled storage account.
    :param bool list:
        Valid for Service and Container resource types only.
    :param bool add:
        Valid for the following Object resource types only: queue messages, and append blobs.
    :param bool create:
        Valid for the following Object resource types only: blobs and files.
        Users can create new blobs or files, but may not overwrite existing
        blobs or files.
    :param bool update:
        Valid for the following Object resource types only: queue messages.
    :param bool process:
        Valid for the following Object resource type only: queue messages.
    :keyword bool tag:
        To enable set or get tags on the blobs in the container.
    :keyword bool filter_by_tags:
        To enable get blobs by tags, this should be used together with list permission.
    :keyword bool set_immutability_policy:
        To enable operations related to set/delete immutability policy.
        To get immutability policy, you just need read permission.
    :keyword bool permanent_delete:
        To enable permanent delete on the blob is permitted.
        Valid for Object resource type of Blob only.
    """

    read: bool = False
    write: bool = False
    delete: bool = False
    delete_previous_version: bool = False
    list: bool = False
    add: bool = False
    create: bool = False
    update: bool = False
    process: bool = False
    tag: bool = False
    filter_by_tags: bool = False
    set_immutability_policy: bool = False
    permanent_delete: bool = False

    def __init__(
        self,
        read: bool = False,
        write: bool = False,
        delete: bool = False,
        list: bool = False,  # pylint: disable=redefined-builtin
        add: bool = False,
        create: bool = False,
        update: bool = False,
        process: bool = False,
        delete_previous_version: bool = False,
        **kwargs
    ) -> None:
        self.read = read
        self.write = write
        self.delete = delete
        self.delete_previous_version = delete_previous_version
        self.permanent_delete = kwargs.pop("permanent_delete", False)
        self.list = list
        self.add = add
        self.create = create
        self.update = update
        self.process = process
        self.tag = kwargs.pop("tag", False)
        self.filter_by_tags = kwargs.pop("filter_by_tags", False)
        self.set_immutability_policy = kwargs.pop("set_immutability_policy", False)
        self._str = (
            ("r" if self.read else "")
            + ("w" if self.write else "")
            + ("d" if self.delete else "")
            + ("x" if self.delete_previous_version else "")
            + ("y" if self.permanent_delete else "")
            + ("l" if self.list else "")
            + ("a" if self.add else "")
            + ("c" if self.create else "")
            + ("u" if self.update else "")
            + ("p" if self.process else "")
            + ("f" if self.filter_by_tags else "")
            + ("t" if self.tag else "")
            + ("i" if self.set_immutability_policy else "")
        )

    def __str__(self):
        return self._str

    @classmethod
    def from_string(cls, permission):
        """Create AccountSasPermissions from a string.

        To specify read, write, delete, etc. permissions you need only to
        include the first letter of the word in the string. E.g. for read and write
        permissions you would provide a string "rw".

        :param str permission: Specify permissions in
            the string with the first letter of the word.
        :return: An AccountSasPermissions object
        :rtype: ~azure.storage.fileshare.AccountSasPermissions
        """
        p_read = "r" in permission
        p_write = "w" in permission
        p_delete = "d" in permission
        p_delete_previous_version = "x" in permission
        p_permanent_delete = "y" in permission
        p_list = "l" in permission
        p_add = "a" in permission
        p_create = "c" in permission
        p_update = "u" in permission
        p_process = "p" in permission
        p_tag = "t" in permission
        p_filter_by_tags = "f" in permission
        p_set_immutability_policy = "i" in permission
        parsed = cls(
            read=p_read,
            write=p_write,
            delete=p_delete,
            delete_previous_version=p_delete_previous_version,
            list=p_list,
            add=p_add,
            create=p_create,
            update=p_update,
            process=p_process,
            tag=p_tag,
            filter_by_tags=p_filter_by_tags,
            set_immutability_policy=p_set_immutability_policy,
            permanent_delete=p_permanent_delete,
        )

        return parsed


class Services(object):
    """Specifies the services accessible with the account SAS.

    :keyword bool blob:
        Access for the `~azure.storage.blob.BlobServiceClient`. Default is False.
    :keyword bool queue:
        Access for the `~azure.storage.queue.QueueServiceClient`. Default is False.
    :keyword bool fileshare:
        Access for the `~azure.storage.fileshare.ShareServiceClient`. Default is False.
    """

    def __init__(self, *, blob: bool = False, queue: bool = False, fileshare: bool = False) -> None:
        self.blob = blob
        self.queue = queue
        self.fileshare = fileshare
        self._str = ("b" if self.blob else "") + ("q" if self.queue else "") + ("f" if self.fileshare else "")

    def __str__(self):
        return self._str

    @classmethod
    def from_string(cls, string):
        """Create Services from a string.

        To specify blob, queue, or file you need only to
        include the first letter of the word in the string. E.g. for blob and queue
        you would provide a string "bq".

        :param str string: Specify blob, queue, or file in
            in the string with the first letter of the word.
        :return: A Services object
        :rtype: ~azure.storage.fileshare.Services
        """
        res_blob = "b" in string
        res_queue = "q" in string
        res_file = "f" in string

        parsed = cls(blob=res_blob, queue=res_queue, fileshare=res_file)
        parsed._str = string
        return parsed


class UserDelegationKey(object):
    """
    Represents a user delegation key, provided to the user by Azure Storage
    based on their Azure Active Directory access token.

    The fields are saved as simple strings since the user does not have to interact with this object;
    to generate an identify SAS, the user can simply pass it to the right API.
    """

    signed_oid: Optional[str] = None
    """Object ID of this token."""
    signed_tid: Optional[str] = None
    """Tenant ID of the tenant that issued this token."""
    signed_start: Optional[str] = None
    """The datetime this token becomes valid."""
    signed_expiry: Optional[str] = None
    """The datetime this token expires."""
    signed_service: Optional[str] = None
    """What service this key is valid for."""
    signed_version: Optional[str] = None
    """The version identifier of the REST service that created this token."""
    value: Optional[str] = None
    """The user delegation key."""

    def __init__(self):
        self.signed_oid = None
        self.signed_tid = None
        self.signed_start = None
        self.signed_expiry = None
        self.signed_service = None
        self.signed_version = None
        self.value = None


class StorageConfiguration(Configuration):
    """
    Specifies the configurable values used in Azure Storage.

    :param int max_single_put_size: If the blob size is less than or equal max_single_put_size, then the blob will be
        uploaded with only one http PUT request. If the blob size is larger than max_single_put_size,
        the blob will be uploaded in chunks. Defaults to 64*1024*1024, or 64MB.
    :param int copy_polling_interval: The interval in seconds for polling copy operations.
    :param int max_block_size: The maximum chunk size for uploading a block blob in chunks.
        Defaults to 4*1024*1024, or 4MB.
    :param int min_large_block_upload_threshold: The minimum chunk size required to use the memory efficient
        algorithm when uploading a block blob.
    :param bool use_byte_buffer: Use a byte buffer for block blob uploads. Defaults to False.
    :param int max_page_size: The maximum chunk size for uploading a page blob. Defaults to 4*1024*1024, or 4MB.
    :param int min_large_chunk_upload_threshold: The max size for a single put operation.
    :param int max_single_get_size: The maximum size for a blob to be downloaded in a single call,
        the exceeded part will be downloaded in chunks (could be parallel). Defaults to 32*1024*1024, or 32MB.
    :param int max_chunk_get_size: The maximum chunk size used for downloading a blob. Defaults to 4*1024*1024,
        or 4MB.
    :param int max_range_size: The max range size for file upload.

    """

    max_single_put_size: int
    copy_polling_interval: int
    max_block_size: int
    min_large_block_upload_threshold: int
    use_byte_buffer: bool
    max_page_size: int
    min_large_chunk_upload_threshold: int
    max_single_get_size: int
    max_chunk_get_size: int
    max_range_size: int
    user_agent_policy: UserAgentPolicy

    def __init__(self, **kwargs):
        super(StorageConfiguration, self).__init__(**kwargs)
        self.max_single_put_size = kwargs.pop("max_single_put_size", 64 * 1024 * 1024)
        self.copy_polling_interval = 15
        self.max_block_size = kwargs.pop("max_block_size", 4 * 1024 * 1024)
        self.min_large_block_upload_threshold = kwargs.get("min_large_block_upload_threshold", 4 * 1024 * 1024 + 1)
        self.use_byte_buffer = kwargs.pop("use_byte_buffer", False)
        self.max_page_size = kwargs.pop("max_page_size", 4 * 1024 * 1024)
        self.min_large_chunk_upload_threshold = kwargs.pop("min_large_chunk_upload_threshold", 100 * 1024 * 1024 + 1)
        self.max_single_get_size = kwargs.pop("max_single_get_size", 32 * 1024 * 1024)
        self.max_chunk_get_size = kwargs.pop("max_chunk_get_size", 4 * 1024 * 1024)
        self.max_range_size = kwargs.pop("max_range_size", 4 * 1024 * 1024)
