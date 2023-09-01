from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class CertTypeChoices(ChoiceSet):
    key = 'Certificate.cert_type'

    STD_OV_SSL = 'standard_ov_ssl'
    ADV_OV_SSL = 'advantage_ov_ssl'
    MULTI_EV_SSL = 'multi-domain_ev_ssl'
    MULTI_OV_SSL = 'multi-domain_ov_ssl'
    WILD_OV_SSL = 'wildcard_ov_ssl'

    CHOICES = [
        ( STD_OV_SSL, "Standard OV SSL", 'green'),
        ( ADV_OV_SSL, "Advantage OV SSL",'orange'),
        ( MULTI_EV_SSL, "Multi-Domain EV SSL",'purple'),
        ( MULTI_OV_SSL, "Multi-Domain OV SSL",'blue'),
        ( WILD_OV_SSL, "Wildcard OV SSL", 'red'),
    ]

class Certificate(NetBoxModel):
    
    cert_type = models.CharField(
        max_length=50,
        choices=CertTypeChoices,
        default=CertTypeChoices.STD_OV_SSL,
        verbose_name=('Certificate Type'),
        help_text=('The Type of the Certificate'),
    )

    common_name = models.CharField(
        max_length=255,
        verbose_name=('Common Name'),
        help_text=('Common Name of the Certificate'),
    )

    SAN_list = models.CharField(
        max_length=1000,
        verbose_name=('SAN List'),
        help_text=('SAN List of the Certificate'),
    )

    issue_date = models.DateField(
        verbose_name=('Certificate Issue Date'),
        help_text=('The Issue Date of the certificate'),
        blank=True, 
        null=True
    )
    expire_date = models.DateField(
        verbose_name=('Certificate Expire Date'),
        help_text=('The Expire Date of the certificate')
    )

    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    virtual_machine = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('common_name', )

    def __str__(self):
        return f"{self.common_name} ({self.SAN_list}): issue:{self.issue_date}, expr:{self.expire_date}"

    def get_cert_type_color(self):
        return CertTypeChoices.colors.get(self.cert_type)

    def get_absolute_url(self):
        return reverse('plugins:netbox_timetable:certificate', args=[self.pk])
    
    def get_platform(self):
        return self.device or self.virtual_machine

    def render_type(self):
        return 'device' if self.device else 'virtual_machine'

