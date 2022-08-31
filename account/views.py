from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm()
    return render(request, "account/login.html", {"form": form})


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form)
        print(form.errors)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect("account-login")
        return render(request, "account/register.html", {"form": form})
    return render(request, "account/register.html", {"form": form})
