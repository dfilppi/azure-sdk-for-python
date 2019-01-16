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

from .secret_bundle_py3 import SecretBundle


class DeletedSecretBundle(SecretBundle):
    """A Deleted Secret consisting of its previous id, attributes and its tags, as
    well as information on when it will be purged.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value: The secret value.
    :type value: str
    :param id: The secret id.
    :type id: str
    :param content_type: The content type of the secret.
    :type content_type: str
    :param attributes: The secret management attributes.
    :type attributes: ~azure.keyvault.v7_1.models.SecretAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :ivar kid: If this is a secret backing a KV certificate, then this field
     specifies the corresponding key backing the KV certificate.
    :vartype kid: str
    :ivar managed: True if the secret's lifetime is managed by key vault. If
     this is a secret backing a certificate, then managed will be true.
    :vartype managed: bool
    :param recovery_id: The url of the recovery object, used to identify and
     recover the deleted secret.
    :type recovery_id: str
    :ivar scheduled_purge_date: The time when the secret is scheduled to be
     purged, in UTC
    :vartype scheduled_purge_date: datetime
    :ivar deleted_date: The time when the secret was deleted, in UTC
    :vartype deleted_date: datetime
    """

    _validation = {
        'kid': {'readonly': True},
        'managed': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SecretAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'kid': {'key': 'kid', 'type': 'str'},
        'managed': {'key': 'managed', 'type': 'bool'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(self, *, value: str=None, id: str=None, content_type: str=None, attributes=None, tags=None, recovery_id: str=None, **kwargs) -> None:
        super(DeletedSecretBundle, self).__init__(value=value, id=id, content_type=content_type, attributes=attributes, tags=tags, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None
