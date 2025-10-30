from django.db import models
from datetime import datetime
class Specialty(models.Model):
    specialty_name=models.CharField(null=False, blank=False,max_length=50)
    def __str__(self):
        return self.specialty_name
    
class Doctor(models.Model):
    name = models.CharField(null=False, blank=False,max_length=50)
    email = models.EmailField(null=False, blank=False,max_length=50)
    qualification = models.CharField(null=False, blank=False,max_length=50)
    specialty = models.ForeignKey(Specialty,on_delete=models.SET_DEFAULT,default=None)
    year_of_experience = models.IntegerField(null=False, blank=False)
    phone_no = models.CharField(null=False, blank=False,max_length=50)
    gender = models.CharField(null=False, blank=False,max_length=10)
    fee = models.CharField(null=False,blank=False,max_length=10,default='1000' )
    time=models.CharField(null=False, blank=False,max_length=10 ,default='00:00')
    password=models.CharField(null=True, blank=False,max_length=10, default='0000')
    added_at = models.DateField(default=datetime.now,null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.specialty.specialty_name}"