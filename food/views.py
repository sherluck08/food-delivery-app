from django.shortcuts import render
from food.models import Food, CustomUser, Cart


def home(request):
    foods = Food.objects.all()
    context = {"foods": foods}
    return render(request, "food/index.html", context=context)


def profile_page(request):
    return render(request, "food/profile.html")


def food_details(request, food_id):
    food = Food.objects.filter(id=food_id).first()
    return render(request, "food/food_details.html", {"food": food})


def checkout(request):
    return render(request, "food/checkout.html")


def add_to_cart(request, user_id, food_id):
    food = Food.objects.filter(id=food_id).get()
    user = CustomUser.objects.filter(id=user_id).get()
    print(food)
    print(user_id)
    check_cart = Cart.objects.filter(order_by=user_id, food=food)
    print(f"{check_cart=}")
    if check_cart:
        print(f"Already added {food.title} to cart")
    else:
        cart = Cart(food=food, order_by=user, price=food.price)
        cart.save()

    return render(request, "food/cart.html")
