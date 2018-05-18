# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class LogFile(ProxyResource):
    """Represents a log file.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param size_in_kb: Size of the log file.
    :type size_in_kb: long
    :ivar created_time: Creation timestamp of the log file.
    :vartype created_time: datetime
    :ivar last_modified_time: Last modified timestamp of the log file.
    :vartype last_modified_time: datetime
    :param log_file_type: Type of the log file.
    :type log_file_type: str
    :param url: The url to download the log file from.
    :type url: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'size_in_kb': {'key': 'properties.sizeInKB', 'type': 'long'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'log_file_type': {'key': 'properties.type', 'type': 'str'},
        'url': {'key': 'properties.url', 'type': 'str'},
    }

    def __init__(self, *, size_in_kb: int=None, log_file_type: str=None, url: str=None, **kwargs) -> None:
        super(LogFile, self).__init__(**kwargs)
        self.size_in_kb = size_in_kb
        self.created_time = None
        self.last_modified_time = None
        self.log_file_type = log_file_type
        self.url = url
