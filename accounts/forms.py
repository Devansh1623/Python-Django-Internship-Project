from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User


class UserRegistrationForm(UserCreationForm):
    # Only allow student and faculty roles during registration
    REGISTRATION_ROLE_CHOICES = [
        ("student", "Student"),
        ("faculty", "Faculty"),
    ]
    
    role = forms.ChoiceField(
        choices=REGISTRATION_ROLE_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    phone = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "+91 XXXXXXXXXX"}),
    )
    date_of_birth = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-input", "type": "date"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "phone",
            "date_of_birth",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-input", "placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"class": "form-input", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": "email@example.com"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ["role"]:
                self.fields[field].widget.attrs["class"] = "form-input"

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered. Please use a different email or login.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-input", "placeholder": "Username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-input", "placeholder": "Password"}),
    )
