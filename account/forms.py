from django import forms
from .models import PatientDetails

class PatientlDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ('first_name', 'last_name', 'age', 'gender', 'contact_info')