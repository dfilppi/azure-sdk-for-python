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

from .cluster_event import ClusterEvent


class ClusterUpgradeRollbackStartEvent(ClusterEvent):
    """Cluster Upgrade Rollback Start event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param target_cluster_version: Required. Target Cluster version.
    :type target_cluster_version: str
    :param failure_reason: Required. Describes failure.
    :type failure_reason: str
    :param overall_upgrade_elapsed_time_in_ms: Required. Overall duration of
     upgrade in milli-seconds.
    :type overall_upgrade_elapsed_time_in_ms: float
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'target_cluster_version': {'required': True},
        'failure_reason': {'required': True},
        'overall_upgrade_elapsed_time_in_ms': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'target_cluster_version': {'key': 'TargetClusterVersion', 'type': 'str'},
        'failure_reason': {'key': 'FailureReason', 'type': 'str'},
        'overall_upgrade_elapsed_time_in_ms': {'key': 'OverallUpgradeElapsedTimeInMs', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(ClusterUpgradeRollbackStartEvent, self).__init__(**kwargs)
        self.target_cluster_version = kwargs.get('target_cluster_version', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.overall_upgrade_elapsed_time_in_ms = kwargs.get('overall_upgrade_elapsed_time_in_ms', None)
        self.kind = 'ClusterUpgradeRollbackStart'
