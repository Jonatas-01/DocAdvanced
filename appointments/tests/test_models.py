from django.test import TestCase
from account.models import PatientDetails, DoctorDetails
from appointments.models import Appointment
from django.contrib.auth import get_user_model