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


class LanguageExampleSuccessTransliteration(Model):
    """LanguageExampleSuccessTransliteration.

    :param language_code:
    :type language_code:
     ~azure.cognitiveservices.translatortext.models.LanguageExampleSuccessTransliterationLanguageCode
    """

    _attribute_map = {
        'language_code': {'key': 'languageCode', 'type': 'LanguageExampleSuccessTransliterationLanguageCode'},
    }

    def __init__(self, **kwargs):
        super(LanguageExampleSuccessTransliteration, self).__init__(**kwargs)
        self.language_code = kwargs.get('language_code', None)
