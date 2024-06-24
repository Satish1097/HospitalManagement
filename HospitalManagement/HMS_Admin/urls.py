from django.urls import path
from . import views


urlpatterns=[
    path("",views.AdminLogin),
    path('ManagePatient',views.ManagePatient, name='ManagePatient'),
    path('ManageDoctor',views.ManageDoctor, name='ManageDoctor'),
    path('DeletePatient/<int:pid>/',views.DeletePatient, name='DeletePatient'),
    path("AdminLogin",views.AdminLogin,name='AdminLogin'),


]