from django import forms
from .models import IncidentReport

class IncidentReportForm(forms.ModelForm):
    class Meta:
        model = IncidentReport
        fields = [
            'first_name', 'last_name', 'job_title', 'department', 'phone', 
            'mobile', 'email', 'date_of_issue', 'severity', 'category', 
            'sub_category', 'device_action', 'source_address', 
            'destination_address', 'destination_port', 'application_protocol', 
            'description','uploaded_image'
        ]
        widgets = {
            'date_of_issue': forms.DateInput(attrs={'type': 'date'}),
            'severity': forms.Select(choices=[
                ('LOW', 'Low'),
                ('MEDIUM', 'Medium'),
                ('HIGH', 'High'),
                ('CRITICAL', 'Critical'),
            ]),
            'category': forms.Select(choices=[
                ('Denial of Service (DoS)', 'Denial of Service (DoS)'),
                ('Exercise-Network Defense Testing', 'Exercise-Network Defense Testing'),
                ('Inappropriate Usage', 'Inappropriate Usage'),
                ('Malicious Code', 'Malicious Code'),
                ('Unauthorized Access', 'Unauthorized Access'),
            ]),
            'uploaded_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@cybertron.co.th'):
            raise forms.ValidationError("Email must end with @cybertron.com")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits")
        return phone