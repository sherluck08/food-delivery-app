from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="account-login"),
    path("register/", views.register, name="account-register"),
]
