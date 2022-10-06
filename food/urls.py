from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="food-homepage"),
    path("<int:food_id>/", views.food_details, name="food-details"),
    path("profile/", views.profile_page, name="food-profile"),
    path("<str:user_id>/cart/<int:food_id>/", views.add_to_cart, name="food-cart"),
    path("<str:user_id>/checkout/<int:food_id>/", views.checkout, name="food-checkout"),
]
