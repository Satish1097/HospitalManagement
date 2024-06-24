from django.db import models
from datetime import date
from django.utils.timezone import now

# Create your models here.
Gender=(
        ('Male','Male'),
        ('Female','Female'),
        ('TransGender','TransGender')
    )

class PatientRegistration(models.Model):
    Name=models.CharField(max_length=30)
    Gender = models.CharField(max_length=20, choices=Gender, verbose_name='Gender')
    email=models.EmailField()
    contact=models.IntegerField(default=0)
    image=models.ImageField(upload_to='images/')
    password=models.CharField(max_length=15)
    DOB=models.DateField(default=now)

    def __str__(self):
        return self.Name
