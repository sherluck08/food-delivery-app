from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django import forms


class CustomUser(AbstractUser):
    username = models.EmailField(_("emai address"), unique=True)
    phone_no = models.CharField(max_length=11)
    is_admin = models.BooleanField("Is admin", default=False)
    account_created_at = models.DateTimeField(auto_now_add=datetime.now)
    delivery_address = models.TextField(default="")
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ("first_name", "last_name", "phone_no")
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
