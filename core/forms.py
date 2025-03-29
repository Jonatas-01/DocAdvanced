from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileCreationForm(UserCreationForm):
    """
    A form for creating new user profiles with role selection.
    This form extends Django's UserCreationForm to include a role
    field and custom styling.
    It allows users to create a new profile by providing a username,
    password, and selecting
    a role from predefined choices.
    """

    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Profile
        fields = ('role', 'username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Create a password'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirm your password'})
