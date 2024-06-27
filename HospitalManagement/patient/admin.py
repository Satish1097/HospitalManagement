from django.contrib import admin
from . models import PatientRegistration,Apointment

# Register your models here.

admin.site.register(PatientRegistration)
admin.site.register(Apointment)