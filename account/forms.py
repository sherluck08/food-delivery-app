from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_no", "first_name", "last_name", "password1", "password2")


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.PasswordInput()
