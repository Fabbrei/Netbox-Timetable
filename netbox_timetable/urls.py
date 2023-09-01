from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import views, models


urlpatterns = [
    # C E R T S
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificates/add/', views.CertificateEditView.as_view(), name='certificate_add'),
    path("certificates/<int:pk>/", views.CertificateView.as_view(), name="certificate"),
    path('certificates/<int:pk>/edit/', views.CertificateEditView.as_view(), name='certificate_edit'),
    path('certificates/<int:pk>/delete/', views.CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certificates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={
        'model': models.Certificate
    }),
]