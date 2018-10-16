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

from .media_job_output_py3 import MediaJobOutput


class MediaJobOutputAsset(MediaJobOutput):
    """The event data for a Job output asset.

    All required parameters must be populated in order to send to Azure.

    :param error: Gets the Job output error.
    :type error: ~azure.eventgrid.models.MediaJobError
    :param label: Gets the Job output label.
    :type label: str
    :param progress: Required. Gets the Job output progress.
    :type progress: long
    :param state: Required. Gets the Job output state. Possible values
     include: 'Canceled', 'Canceling', 'Error', 'Finished', 'Processing',
     'Queued', 'Scheduled'
    :type state: str or ~azure.eventgrid.models.MediaJobState
    :param asset_name: Gets the Job output asset name.
    :type asset_name: str
    """

    _validation = {
        'progress': {'required': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'MediaJobError'},
        'label': {'key': 'label', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'long'},
        'state': {'key': 'state', 'type': 'MediaJobState'},
        'asset_name': {'key': 'assetName', 'type': 'str'},
    }

    def __init__(self, *, progress: int, state, error=None, label: str=None, asset_name: str=None, **kwargs) -> None:
        super(MediaJobOutputAsset, self).__init__(error=error, label=label, progress=progress, state=state, **kwargs)
        self.asset_name = asset_name
