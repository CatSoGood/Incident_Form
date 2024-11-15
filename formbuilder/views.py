from django.shortcuts import render, redirect
from .forms import IncidentReportForm

def create_incident_report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incident_report_success')
    else:
        form = IncidentReportForm()
    return render(request, 'formbuilder/incident_report_form.html', {'form': form})

def incident_report_success(request):
    return render(request, 'formbuilder/incident_report_success.html')
