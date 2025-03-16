from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments_view, name='appointments'),
    path('request/<int:doctor_id>/', views.request_appointment, name='request_appointment'),
]