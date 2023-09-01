from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import CertificateSerializer, PowerSerializer


class CertificateViewSet(NetBoxModelViewSet):
    queryset = models.Certificate.objects.prefetch_related('tags').all()
    serializer_class = CertificateSerializer

