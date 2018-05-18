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

from msrest.serialization import Model


class DeviceTwinProperties(Model):
    """A portion of the properties that can be written only by the application
    back-end, and read by the device.

    :param metadata: Metadata information for the properties JSON document.
    :type metadata: ~azure.eventgrid.models.DeviceTwinMetadata
    :param version: Version of device twin properties.
    :type version: float
    """

    _attribute_map = {
        'metadata': {'key': 'metadata', 'type': 'DeviceTwinMetadata'},
        'version': {'key': 'version', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(DeviceTwinProperties, self).__init__(**kwargs)
        self.metadata = kwargs.get('metadata', None)
        self.version = kwargs.get('version', None)
