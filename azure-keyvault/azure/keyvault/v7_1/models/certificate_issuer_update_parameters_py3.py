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


class CertificateIssuerUpdateParameters(Model):
    """The certificate issuer update parameters.

    :param provider: The issuer provider.
    :type provider: str
    :param credentials: The credentials to be used for the issuer.
    :type credentials: ~azure.keyvault.v7_1.models.IssuerCredentials
    :param organization_details: Details of the organization as provided to
     the issuer.
    :type organization_details:
     ~azure.keyvault.v7_1.models.OrganizationDetails
    :param attributes: Attributes of the issuer object.
    :type attributes: ~azure.keyvault.v7_1.models.IssuerAttributes
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'credentials': {'key': 'credentials', 'type': 'IssuerCredentials'},
        'organization_details': {'key': 'org_details', 'type': 'OrganizationDetails'},
        'attributes': {'key': 'attributes', 'type': 'IssuerAttributes'},
    }

    def __init__(self, *, provider: str=None, credentials=None, organization_details=None, attributes=None, **kwargs) -> None:
        super(CertificateIssuerUpdateParameters, self).__init__(**kwargs)
        self.provider = provider
        self.credentials = credentials
        self.organization_details = organization_details
        self.attributes = attributes
