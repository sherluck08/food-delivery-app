from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "phone_no", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        username = self.cleaned_data.get("username")
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This email is already used")
        return username


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.PasswordInput()

    class Meta:
        fields = ("email", "password")
