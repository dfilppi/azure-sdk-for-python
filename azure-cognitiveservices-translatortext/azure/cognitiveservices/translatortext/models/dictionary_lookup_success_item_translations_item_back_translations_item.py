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


class DictionaryLookupSuccessItemTranslationsItemBackTranslationsItem(Model):
    """DictionaryLookupSuccessItemTranslationsItemBackTranslationsItem.

    :param normalized_text:
    :type normalized_text: str
    :param display_text:
    :type display_text: str
    :param num_examples:
    :type num_examples: int
    :param frequency_count:
    :type frequency_count: int
    """

    _attribute_map = {
        'normalized_text': {'key': 'normalizedText', 'type': 'str'},
        'display_text': {'key': 'displayText', 'type': 'str'},
        'num_examples': {'key': 'numExamples', 'type': 'int'},
        'frequency_count': {'key': 'frequencyCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(DictionaryLookupSuccessItemTranslationsItemBackTranslationsItem, self).__init__(**kwargs)
        self.normalized_text = kwargs.get('normalized_text', None)
        self.display_text = kwargs.get('display_text', None)
        self.num_examples = kwargs.get('num_examples', None)
        self.frequency_count = kwargs.get('frequency_count', None)
