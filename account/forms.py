from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_no", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already used")
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.PasswordInput()

    class Meta:
        fields = ("email", "password")
