from django.shortcuts import render,redirect,HttpResponse
from . models import PatientRegistration
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import appointment_form
from .models import Apointment

# Create your views here.
def Home(req):
    return render(req,"home.html")
def PatientRegister(req):
    if req.method=='GET':
        return render(req,"PatientRegistration.html")
    else:
        Name=req.POST.get('name')
        Gender=req.POST.get('gender')
        email=req.POST.get('email')
        contact=req.POST.get('contact')
        image=req.FILES.get('image')
        password=req.POST.get('password')
        
        if PatientRegistration.objects.filter(email=email):
            msg="Already exist"
            return render(req,'Home',{'msg':msg})
        else:
            PatientRegistration.objects.create(
                Name=Name,
                Gender=Gender,
                email=email,
                contact=contact,
                image=image,
                password=password
            )
            return redirect('/')
        
def PatientLogin(req):
    if req.method=='GET':
        return render(req,'PatientLogin.html')
    else:
        email=req.POST.get('email')
        password=req.POST.get('password')

        patientValidate=PatientRegistration.objects.get(email=email, password=password)
        if(patientValidate):
            x=req.session['PatientId']=patientValidate.id
            return redirect('PatientProfile')
        else:
            return HttpResponse("doesn't Exist")
@login_required
def PatientProfile(req):
    patient_id = req.session.get('PatientId')
    if(patient_id):
        patient = get_object_or_404(PatientRegistration, id=patient_id)
        context = {'patient': patient}
        return render(req,'PatientProfile.html', context)

def PatientUpdate(req,pid):
    data=PatientRegistration.objects.get(id=pid)
    return render(req,'PatientUpdateForm.html',{"data":data})
def PatientUpdateSave(req,pid):
    patient=PatientRegistration.objects.get(id=pid)
    patient.Name=req.POST.get('name')
    patient.Gender=req.POST.get('gender')
    patient.email=req.POST.get('email')
    patient.contact=req.POST.get('contact')
    patient.image=req.FILES.get('image')
    patient.password=req.POST.get('password')
    
    patient.save()
    return redirect('PatientProfile')

@login_required
def PatientApointment(request):
    if request.method == 'POST':
        form = appointment_form(request.POST)
        if form.is_valid():
            blood_group = form.cleaned_data.get('Blood_Group')
            disease = form.cleaned_data.get('Disease')

            # Get the patient from the session
            patient_id = request.session.get('PatientId')
            if patient_id:
                try:
                    patient = PatientRegistration.objects.get(id=patient_id)
                    Apointment.objects.create(
                        Blood_Group=blood_group,
                        Disease=disease,
                        Name=patient  # Properly associating the patient
                    )
                    return redirect('AppointmentDetail')
                except PatientRegistration.DoesNotExist:
                    return HttpResponse("Patient does not exist")
            else:
                return HttpResponse("No patient is logged in")

    else:
        form = appointment_form()
    return render(request, 'Apointmentform.html', {'form': form})

def AppointmentDetail(req):
    patient_id = req.session.get('PatientId')
    if patient_id:
        try:
            data = Apointment.objects.get(id=patient_id)
            return render(req, 'PatientApointmentDetail.html', {'data': data})
        except Apointment.DoesNotExist:
            return render(req, 'PatientApointmentDetail.html', {'error': 'Appointment not found'})
    return render(req, 'PatientApointmentDetail.html', {'error': 'Patient ID not found in session'})

def AppointmentPayment(req):
    return HttpResponse('Pay your fee')