from django.forms import ModelForm
from food.models import Food


class AddToMenuForm(ModelForm):
    class Meta:
        model = Food
        fields = ("title", "description", "price", "image", "category")
