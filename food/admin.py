from django.contrib import admin
from .models import Category, Order, Food

# Register your models here.

admin.site.register([Category, Order, Food])
