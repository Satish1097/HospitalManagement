from django.shortcuts import render,redirect,HttpResponse
from .models import Doctor

# Create your views here.

def DoctorLogin(req):
    if req.method=="GET":
        return render(req,"DoctorLogin.html")
    else:
        AdminId=req.POST.get('doctorId')
        Password=req.POST.get('password')
        doctor=Doctor.objects.filter(AdminId=AdminId,Password=Password)
        if(doctor):
            return HttpResponse('logged In')