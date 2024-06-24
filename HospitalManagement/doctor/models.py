from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.
class Doctor(models.Model):
    Name=models.CharField( max_length=50)
    DoctorId=models.CharField(max_length=10) 
    DOJ=models.DateField(default=now)
    Gender=models.CharField(max_length=15)
    Speciality=models.CharField(max_length=50)
    Password=models.CharField(max_length=18)

    def __str__(self):
        return self.Name