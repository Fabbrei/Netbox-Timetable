from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Certificate


#
# Nested serializers
#

class NestedCertificateSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_timetable-api:certificate-detail'
    )

    class Meta:
        model = Certificate
        fields = ('id', 'url', 'display', 'cert_type', 'common_name', 'SAN_list', 'issue_date', 'expire_date', 'device', 'virtual_machine', 'tags', 'custom_fields', 'created', 'last_updated')


#
# Regular serializers
#

class CertificateSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_timetable-api:certificate-detail'
    )

    class Meta:
        model = Certificate
        fields = (
            'id', 'url', 'display', 'cert_type', 'common_name', 'SAN_list', 'issue_date', 'expire_date', 'tags', 'custom_fields', 'created',
            'last_updated',
        )
