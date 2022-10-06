from django.shortcuts import render, redirect
from account.models import CustomUser
from food.models import Food, Order
from .forms import AddToMenuForm
from django.contrib import messages


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
            menu_form.save()
            title = request.POST.get("title")
            messages.success(request, f"successfully added {title} to the menu")
            return redirect("admin_page-menus")
        else:
            messages.error(request, f"unable to add item to the menu, {menu_form.errors}")
            return redirect("admin_page-add-to-menu")
    menu_form = AddToMenuForm()
    return render(request, "admin_page/add_to_menu.html", {"menu_form": menu_form})


def menus(request):
    foods = Food.objects.all()
    return render(request, "admin_page/menus.html", {"foods": foods})


def menu(request, menu_id):
    print(menu_id)
    return render(request, "admin_page/menu.html")


def delete_menu(request, menu_id):
    food = Food.objects.filter(id=menu_id)
    food.delete()
    return redirect("admin_page-menus")


def update_menu(request, menu_id):
    food = Food.objects.get(id=menu_id)
    if request.method == "POST":
        menu_form = AddToMenuForm(request.POST, request.FILES)
        if menu_form.is_valid():
            menu_form = AddToMenuForm(instance=food)
            return redirect("admin_page-menus")
        else:
            messages.error(request, f"unable to add item to the menu, {menu_form.errors}")
            return redirect("admin_page-update-menu")
    menu_form = AddToMenuForm()
    return render(request, "admin_page/update_menu.html", {"food": food, "menu_form": menu_form})


def get_orders(request):

    return render(request, "admin_page/order.html")


def add_admin(request):
    return render(request, "admin_page/add_admin.html")
