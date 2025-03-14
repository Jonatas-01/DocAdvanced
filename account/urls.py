from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_view, name='account-details'),
    path('patient-form/', views.patient_details_form, name='patient-form'),
    path('doctor-form/', views.doctor_details_form, name='doctor-form'),
    path('edit-details/', views.edit_details, name='edit-details'),
]