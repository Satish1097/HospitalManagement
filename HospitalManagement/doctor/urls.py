from django.urls import path
from . import views

urlpatterns= [
    path("",views.DoctorLogin, name="DoctorLogin"),
]