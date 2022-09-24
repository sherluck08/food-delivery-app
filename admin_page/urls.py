from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="admin_page-homepage"),
    path("add-to-menu/", views.add_to_menu, name="admin_page-add-to-menu"),
    path("menu/", views.menu, name="admin_page-menu"),
]
