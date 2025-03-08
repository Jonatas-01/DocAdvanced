from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('role', 'username', 'password1', 'password2')
