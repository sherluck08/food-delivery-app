from django.db import models
from account.models import CustomUser
import datetime
import uuid


class Food(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    price = models.FloatField(null=False)
    availability = models.BooleanField(default=True)
    image = models.ImageField()
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    DRINKS_AND_BEVERAGES = "Drinks and Beverages"
    MEAT = "Meat"
    SIDE_DISH = "Side Dish"
    SNACKS = "Snacks"
    CHICKEN = "Chicken"
    OTHER = "other"

    category_choices = (
        (DRINKS_AND_BEVERAGES, DRINKS_AND_BEVERAGES),
        (MEAT, MEAT),
        (SIDE_DISH, SIDE_DISH),
        (SNACKS, SNACKS),
        (CHICKEN, CHICKEN),
        (OTHER, OTHER),
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    order_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(name="Quantity")
    date_order = models.DateTimeField(auto_now_add=datetime.datetime)
    order_started = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
