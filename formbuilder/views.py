from django.shortcuts import render, redirect
from .forms import IncidentReportForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from datetime import datetime, date

def create_incident_report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'date_of_issue' in data and isinstance(data['date_of_issue'], date):
                data['date_of_issue'] = data['date_of_issue'].isoformat()
            request.session['form_data'] = data
            return redirect('preview_incident_report')
        else:
            print("Form errors:", form.errors)
    else:
        form = IncidentReportForm()
    return render(request, 'formbuilder/incident_report_form.html', {'form': form})

def preview_incident_report(request):
    data = request.session.get('form_data')
    if not data:
        return redirect('create_incident_report')
    
    if 'date_of_issue' in data:
        data['date_of_issue'] = datetime.fromisoformat(data['date_of_issue']).date()
    
    return render(request, 'formbuilder/incident_report_preview.html', {'data': data})

def download_pdf(request):
    data = request.session.get('form_data')  # ดึงข้อมูลจาก session
    if not data:  # หากไม่มีข้อมูล
        return redirect('create_incident_report')  # Redirect กลับไปหน้าแรก
    html = render_to_string('formbuilder/incident_report_preview.html', {'data': data})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="incident_report.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

def incident_report_success(request):
    return render(request, 'formbuilder/incident_report_success.html')