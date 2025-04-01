from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True)
    subscription_status = models.CharField(max_length=50, default='inactive')

    def __str__(self):
        return self.username
