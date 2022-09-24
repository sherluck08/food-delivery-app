from django.shortcuts import render, redirect
from account.models import CustomUser
from food.models import Food, Order
from .forms import AddToMenuForm


def home(request):
    user_count = CustomUser.objects.count()
    no_of_foods = Food.objects.count()
    no_of_orders = Order.objects.count()
    context = {"user_count": user_count, "no_of_foods": no_of_foods, "no_of_orders": no_of_orders}
    return render(request, "admin_page/admin.html", context)


def add_to_menu(request):
    if request.method == "POST":
        menu_form = AddToMenuForm(request.POST, request.FILES)
        if menu_form.is_valid():
            print("Menu form is valid")
            menu_form.save()
            return redirect("admin_page-menu")
        else:
            print("Menu form is not valid")
            print(menu_form.errors)
    menu_form = AddToMenuForm()
    return render(request, "admin_page/add_to_menu.html", {"menu_form": menu_form})


def menu(request):
    foods = Food.objects.all()
    return render(request, "admin_page/menu.html", {"foods": foods})
