from django import forms
from .models import PatientDetails, DoctorDetails


class PatientlDetailsForm(forms.ModelForm):
    """
    Form for patient details including personal and medical information.
    Used for creating and updating patient records with fields for basic
    personal data, medical history, and allergies.
    """

    class Meta:

        model = PatientDetails
        fields = ('first_name', 'last_name', 'age', 'gender',
                  'contact_info', 'medical_history', 'allergies')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact_info': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'medical_history': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your medical history', 'rows': 2}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List any allergies', 'rows': 2}),
        }


class DoctorDetailsForm(forms.ModelForm):
    """
    Form for doctor profile details.
    This form allows doctors to input and update their personal and professional information.
    It includes fields for name, gender, contact information, medical specialty, and a brief bio.
    """

    class Meta:
        model = DoctorDetails
        fields = ('first_name', 'last_name', 'gender',
                  'contact_info', 'specialty', 'about')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact_info': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'specialty': forms.Select(attrs={'class': 'form-select'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell us a bit about yourself and your methods, try keep it simple.', 'rows': 5}),
        }
