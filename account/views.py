from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            print("User is successfully logged in")
            return redirect("account-login")

    return render(request, "account/login.html")


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
