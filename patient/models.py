from django.db import models
from datetime import datetime
from doctor.models import Doctor

class Patient(models.Model):
    name = models.CharField(null=False,blank=False,max_length=255)
    email = models.EmailField(null=False,blank=False,max_length=50)
    phone_number = models.CharField(null=False,blank=False,max_length=20)
    gender=models.CharField(null=False,blank=False,max_length=20)
    age=models.CharField(null=False,blank=False,max_length=20)
    password=models.CharField(null=True, blank=False,max_length=10, default='0000')
    added_at = models.DateField(default=datetime.now,null=False, blank=False)
    def __str__(self):
        return self.name
class Appointment(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE,default=None)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=None)
    issue=models.CharField(null=False,blank=False,max_length=255,default=None)
    appointment_date = models.DateTimeField(default=datetime.now,null=False, blank=False)
    status = models.CharField(null=False,blank=False,max_length=255,default=None)
# Create your models here.
    def __str__(self):
        return f"Appointment ID: {self.id}"

