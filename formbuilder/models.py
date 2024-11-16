from django.db import models

class IncidentReport(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_issue = models.DateField()
    severity = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    device_action = models.CharField(max_length=100)
    source_address = models.CharField(max_length=100)
    destination_address = models.CharField(max_length=100)
    destination_port = models.CharField(max_length=10)
    application_protocol = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date_of_issue}"
