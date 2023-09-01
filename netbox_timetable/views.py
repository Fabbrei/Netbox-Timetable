from netbox.views import generic
from . import filtersets, forms, tables, models



### C E R T I F I C A T E 

class CertificateView(generic.ObjectView):
    queryset = models.Certificate.objects.all()


class CertificateListView(generic.ObjectListView):
    queryset = models.Certificate.objects.all()
    table = tables.CertificateTable
    filterset = filtersets.CertificateFilterSet
    filterset_form = forms.CertificateFilterSetForm


class CertificateEditView(generic.ObjectEditView):
    queryset = models.Certificate.objects.all()
    form = forms.CertificateForm


class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = models.Certificate.objects.all()

