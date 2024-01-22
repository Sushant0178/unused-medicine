from django.contrib import admin
from django.urls import path, include
from . import views
from .models import ngodetail, donordetail, medicine, doctordetail
from .forms import CreateUserForm, CreatengoForm, CreateDoctorForm
from .forms import CreateUserForm, CreatengoForm, CreateDoctorForm
urlpatterns = [
    path('', views.index, name='home'),
    path('registerdonor/', views.registerdonor, name="registerdonor"),
    path('registerseller/', views.registerseller, name="registerseller"),
    path('registerngo/', views.registerngo, name="registerngo"),
    path('login/', views.loginpage, name="login"),  
    path('logout/', views.logoutuser, name="logout"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contact/', views.contact, name="contact"),
    path('NGO-Details/', views.detailsngo, name="detailsngo"),
    path('Donor-Details/', views.detailsdonor, name="detailsdonor"),
    path('adminaction/', views.adminaction, name="adminaction"),
    path('admindashboard/', views.admindashboard, name="admindashboard"),
    path('NGOdashboard/', views.ngodashboard, name="ngodashboard"),
    path('donordashboard/', views.donordashboard, name="donordashboard"),
    path('donorprofile/', views.donorprofile, name="donorprofile"),
    path('ngoprofile/', views.ngoprofile, name="ngoprofile"),
    path('medicinedonation/', views.medicinedonation, name="medicinedonation"),
    path('registerdoctor/', views.Registerdoctor, name='registerdoctor'),
    # path('thankyou/', views.thankyou, name='thankyou'),
    path('search_ngos/', views.search_ngos,name='search_ngos')
    
    # Use views.Registerdoctor instead of Registerdoctor
    # path('registerdoctor/', RegisterDoctorView.as_view(), name='registerdoctor'),
    #  path('', HomePageView.as_view(), name='home'),
    
    
]
