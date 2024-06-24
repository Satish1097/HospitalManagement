from django.shortcuts import render,redirect,HttpResponse
from patient.models import PatientRegistration
from doctor.models import Doctor
from . models import Admin
from django.urls import reverse
# Create your views here.

def AdminLogin(req):
    if req.method=='GET':
        return render(req,'AdminLogin.html')
    else:
        AdminId=req.POST.get('admin_id')
        Password=req.POST.get('password')
        AdminCheck=Admin.objects.filter(AdminId=AdminId,Password=Password)
        if(AdminCheck):
            return render(req,'Admin.html')
        else:
            msg= "wrong Credential"
            return render(req,'AdminLogin.html',{'msg':msg})

def ManagePatient(req):
    patients=PatientRegistration.objects.all()
    return render(req,'PatientRecord.html',{'patients':patients})

def ManageDoctor(req):
    doctors=Doctor.objects.all()
    return render(req,'DoctorRecord.html',{"doctors":doctors})
def DeletePatient(req,pid):
    data1=PatientRegistration.objects.filter(id=pid)
    data1.delete()
    return redirect(reverse('ManagePatient'))
