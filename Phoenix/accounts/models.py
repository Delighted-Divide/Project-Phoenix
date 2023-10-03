import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10, choices=[(
        'Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True)
