from netbox.filtersets import NetBoxModelFilterSet
from .models import Certificate

class CertificateFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = Certificate
        fields = ("cert_type", "common_name", "SAN_list", "issue_date", "expire_date")

    def search(self, queryset, name, value):
        return queryset.filter(common_name__icontains=value)
