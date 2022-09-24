from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("User is successfully logged in")
            return redirect("food-homepage")

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


def log_out(request):
    logout(request)
    return redirect("account-login")
