from django import forms
from .models import PatientDetails, DoctorDetails

class PatientlDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ('first_name', 'last_name', 'age', 'gender', 'contact_info')


class DoctorDetailsForm(forms.ModelForm):
    class Meta:
        model = DoctorDetails
        fields = ('first_name', 'last_name', 'gender', 'contact_info', 'specialty', 'about')