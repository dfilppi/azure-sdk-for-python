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


class LastDetectResponse(Model):
    """LastDetectResponse.

    :param period: Frequency extracted from the series, zero means no
     recurrent pattern has been found.
    :type period: int
    :param suggested_window: Suggested input series points needed for
     detecting the latest point.
    :type suggested_window: int
    :param expected_value: Expected value of the latest point.
    :type expected_value: float
    :param upper_margin: Upper margin of the latest point. UpperMargin is used
     to calculate upperBoundary, which equals to expectedValue + (100 -
     sensitivity)*upperMargin. If the value of latest point is between
     upperBoudary and lowerBoudary, it should be treated as normal value. By
     adjusting sensitivity value, anomaly status of latest point can be
     changed.
    :type upper_margin: float
    :param lower_margin: Lower margin of the latest point. LowerMargin is used
     to calculate lowerBoundary, which equals to expectedValue - (100 -
     sensitivity)*lowerMargin.
    :type lower_margin: float
    :param is_anomaly: Anomaly status of the latest point, true means the
     latest point is an anomaly either in negative direction or positive
     direction.
    :type is_anomaly: bool
    :param is_negative_anomaly: Anomaly status in negative direction of the
     latest point. True means the latest point is an anoamly and its real value
     is smaller than the expected one.
    :type is_negative_anomaly: bool
    :param is_positive_anomaly: Anomaly status in positive direction of the
     latest point. True means the latest point is an anomaly and its real value
     is larger than the expected one.
    :type is_positive_anomaly: bool
    """

    _attribute_map = {
        'period': {'key': 'period', 'type': 'int'},
        'suggested_window': {'key': 'suggestedWindow', 'type': 'int'},
        'expected_value': {'key': 'expectedValue', 'type': 'float'},
        'upper_margin': {'key': 'upperMargin', 'type': 'float'},
        'lower_margin': {'key': 'lowerMargin', 'type': 'float'},
        'is_anomaly': {'key': 'isAnomaly', 'type': 'bool'},
        'is_negative_anomaly': {'key': 'isNegativeAnomaly', 'type': 'bool'},
        'is_positive_anomaly': {'key': 'isPositiveAnomaly', 'type': 'bool'},
    }

    def __init__(self, *, period: int=None, suggested_window: int=None, expected_value: float=None, upper_margin: float=None, lower_margin: float=None, is_anomaly: bool=None, is_negative_anomaly: bool=None, is_positive_anomaly: bool=None, **kwargs) -> None:
        super(LastDetectResponse, self).__init__(**kwargs)
        self.period = period
        self.suggested_window = suggested_window
        self.expected_value = expected_value
        self.upper_margin = upper_margin
        self.lower_margin = lower_margin
        self.is_anomaly = is_anomaly
        self.is_negative_anomaly = is_negative_anomaly
        self.is_positive_anomaly = is_positive_anomaly
