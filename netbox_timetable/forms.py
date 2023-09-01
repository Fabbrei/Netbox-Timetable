from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import Certificate, CertTypeChoices
from utilities.forms.widgets import DatePicker
from utilities.forms.fields import DynamicModelChoiceField
from dcim.models import Device
from virtualization.models import VirtualMachine


class CertificateForm(NetBoxModelForm):
    
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        required=False,
    )
    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
    )

    issue_date = forms.DateField(
        help_text=('The Issue Date of the certificate'),
        required=False,
        widget=DatePicker())
    
    expire_date = forms.DateField(
        help_text=('The Expire Date of the certificate'),
        widget=DatePicker())

    class Meta:
        model = Certificate
        fields = ("device", "virtual_machine", "cert_type", "common_name", "SAN_list", "issue_date", "expire_date", "tags")

class CertificateFilterSetForm(NetBoxModelFilterSetForm):
    model = Certificate

    cert_type = forms.MultipleChoiceField(
        choices=CertTypeChoices,
        required=False
    )

    common_name = forms.CharField(
        required=False
    )

    SAN_list = forms.CharField(
        required=False
    )

    expire_date = forms.DateField(
        required=False
    )

