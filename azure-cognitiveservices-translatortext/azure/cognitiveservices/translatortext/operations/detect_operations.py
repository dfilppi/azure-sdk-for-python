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

from msrest.pipeline import ClientRawResponse

from .. import models


class DetectOperations(object):
    """DetectOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def detect_post(
            self, api_version, text, ocp_apim_subscription_key=None, client_trace_id=None, custom_headers=None, raw=False, **operation_config):
        """Identifies the language of a string of text.
        .

        :param api_version: Version of the API requested by the client. Value
         must be **3.0**.
        :type api_version: str
        :param text: # Request Body
         The body of the request is a JSON array. Each array element is a JSON
         object with a string property named Text. Language detection is
         applied to the value of the Text property.
         The following limitations apply:
         * The array can have at most 100 elements.
         * The text value of an array element cannot exceed 10,000 characters
         including spaces.
         * The entire text included in the request cannot exceed 50,000
         characters including spaces.
         # Response Body
         A successful response is a JSON array with one result for each string
         in the input array. A result object includes the following properties:
         * language- Code of the detected language.
         * score- A float value indicating the confidence in the result. The
         score is between zero and one and a low score indicates a low
         confidence.
         * isTranslationSupported- A boolean value which is true if the
         detected language is one of the languages supported for text
         translation. Not all detected languages can be translated by the API.
         * isTransliterationSupported- A boolean value which is true if the
         detected language is one of the languages supported for
         transliteration.
         * alternatives- An array of other possible languages. Each element of
         the array is another object with the same properties listed above-
         language, score, isTranslationSupported and
         isTransliterationSupported.
         # Response Header
         X-RequestId - Value generated by the service to identify the request.
         It is used for troubleshooting purposes.
        :type text:
         list[~azure.cognitiveservices.translatortext.models.DetectTextInput]
        :param ocp_apim_subscription_key: This is used to pass a key for auth.
         If you are passing a token for auth then use the previous header auth
         option. **ONE OF THESE METHODS MUST BE USED.**
        :type ocp_apim_subscription_key: str
        :param client_trace_id: A client-generated GUID to uniquely identify
         the request. Note that you can omit this header if you include the
         trace ID in the query string using a query parameter named
         ClientTraceId.
        :type client_trace_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype:
         list[~azure.cognitiveservices.translatortext.models.DetectSuccessItem]
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorMessageException<azure.cognitiveservices.translatortext.models.ErrorMessageException>`
        """
        # Construct URL
        url = self.detect_post.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if ocp_apim_subscription_key is not None:
            header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("ocp_apim_subscription_key", ocp_apim_subscription_key, 'str')
        if client_trace_id is not None:
            header_parameters['ClientTraceId'] = self._serialize.header("client_trace_id", client_trace_id, 'str')

        # Construct body
        body_content = self._serialize.body(text, '[DetectTextInput]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorMessageException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[DetectSuccessItem]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    detect_post.metadata = {'url': '/Detect'}
