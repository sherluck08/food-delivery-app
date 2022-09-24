from django.shortcuts import render
from food.models import Food


def home(request):
    foods = Food.objects.all()
    context = {"foods": foods}
    return render(request, "food/index.html", context=context)
