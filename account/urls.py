from django.urls import path
from . import views

urlpatterns = [
    path('patient-form/', views.patient_details_form, name='patient-form'),
]