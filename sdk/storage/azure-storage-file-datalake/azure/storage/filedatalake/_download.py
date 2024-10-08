# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import IO, Iterator, Optional

from ._deserialize import from_blob_properties


class StorageStreamDownloader(object):
    """A streaming object to download from Azure Storage.

    :ivar str name:
        The name of the file being downloaded.
    :ivar ~azure.storage.filedatalake.FileProperties properties:
        The properties of the file being downloaded. If only a range of the data is being
        downloaded, this will be reflected in the properties.
    :ivar int size:
        The size of the total data in the stream. This will be the byte range if specified,
        otherwise the total size of the file.
    """

    def __init__(self, downloader):
        self._downloader = downloader
        self.name = self._downloader.name

        # Parse additional Datalake-only properties
        encryption_context = self._downloader._response.response.headers.get('x-ms-encryption-context')
        acl = self._downloader._response.response.headers.get('x-ms-acl')

        self.properties = from_blob_properties(
            self._downloader.properties,
            encryption_context=encryption_context,
            acl=acl)
        self.size = self._downloader.size

    def __len__(self):
        return self.size

    def chunks(self) -> Iterator[bytes]:
        """Iterate over chunks in the download stream.

        :returns: An iterator containing the chunks in the download stream.
        :rtype: Iterator[bytes]
        """
        return self._downloader.chunks()

    def read(self, size: Optional[int] = -1) -> bytes:
        """
        Read up to size bytes from the stream and return them. If size
        is unspecified or is -1, all bytes will be read.

        :param int size:
            The number of bytes to download from the stream. Leave unspecified
            or set to -1 to download all bytes.
        :returns:
            The requested data as bytes. If the return value is empty, there is no more data to read.
        :rtype: bytes
        """
        return self._downloader.read(size)

    def readall(self) -> bytes:
        """Download the contents of this file.

        This operation is blocking until all data is downloaded.
        :returns: The contents of the specified file.
        :rtype: bytes
        """
        return self._downloader.readall()

    def readinto(self, stream: IO[bytes]) -> int:
        """Download the contents of this file to a stream.

        :param IO[bytes] stream:
            The stream to download to. This can be an open file-handle,
            or any writable stream. The stream must be seekable if the download
            uses more than one parallel connection.
        :returns: The number of bytes read.
        :rtype: int
        """
        return self._downloader.readinto(stream)
