from django.shortcuts import render, redirect, HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('PatientRegister/', views.PatientRegister, name='PatientRegister'),
    path('PatientLogin',views.PatientLogin, name='PatientLogin'),
    path('PatientProfile/', views.PatientProfile, name='PatientProfile'),
    path('PatientUpdate/<int:pid>/',views.PatientUpdate, name='PatientUpdate'),
    path('PatientUpdateSave<int:pid>',views.PatientUpdateSave, name='PatientUpdateSave'),
    path('PatientApointment',views.PatientApointment,name='PatientApointment'),
    path('AppointmentDetail',views.AppointmentDetail,name='AppointmentDetail'),
    path('AppointmentPayment',views.AppointmentPayment,name='AppointmentPayment'),

]
