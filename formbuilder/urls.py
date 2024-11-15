from django.urls import path
from . import views

urlpatterns = [
    path('incident-report/', views.create_incident_report, name='create_incident_report'),
    path('incident-report/success/', views.incident_report_success, name='incident_report_success'),
]
