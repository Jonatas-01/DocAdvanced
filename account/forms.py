from django import forms
from .models import PatientDetails, DoctorDetails


class PatientlDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ('first_name', 'last_name', 'age', 'gender', 'contact_info')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact_info': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
        }


class DoctorDetailsForm(forms.ModelForm):
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
