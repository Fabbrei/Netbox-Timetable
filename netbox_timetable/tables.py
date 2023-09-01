import django_tables2 as tables
from .models import Certificate
from netbox.tables import NetBoxTable, columns, ChoiceFieldColumn, MarkdownColumn
from django_tables2.utils import Accessor

class CertificateTable(NetBoxTable):
    common_name = tables.Column(linkify=True)
    device = tables.Column(
        accessor=Accessor('device'),
        linkify=True
    )
    virtual_machine = tables.Column(
        accessor=Accessor('virtual_machine'),
        linkify=True
    )

    cert_type = ChoiceFieldColumn()

    tags = columns.TagColumn(
        url_name="plugins:netbox_timetable:certificate_list",
    )
    class Meta(NetBoxTable.Meta):
        model = Certificate
        fields = ('pk', 'id', 'cert_type', 'common_name', 'SAN_list', 'issue_date', 'expire_date', 'device', 'virtual_machine', 'tags')
        default_columns = ('common_name', 'SAN_list', 'issue_date', 'expire_date', 'cert_type', 'tags')
