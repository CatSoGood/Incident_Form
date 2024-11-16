from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_incident_report, name='create_incident_report'),
    path('success', views.incident_report_success, name='incident_report_success'),
    path('preview', views.preview_incident_report, name='preview_incident_report'),
    path('download', views.download_pdf, name='download_pdf'),
]
