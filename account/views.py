from django.shortcuts import render
from .forms import LoginForm


def login_view(request):
    if request.method == "POST":
        return LoginForm()
    else:
        return LoginForm()


def register(request):
    return render(request, "account/register.html")
