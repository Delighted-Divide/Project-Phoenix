from typing import Any
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import default_storage

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
    date_of_employment = models.DateField(auto_now_add=True)
    nationality = models.CharField(max_length=100, default='US')
    language = models.CharField(max_length=100, default='English')
    marital_status = models.CharField(max_length=50, default='Married', choices=[
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Other', 'Other'),
    ])
    hobby = models.CharField(max_length=255, default='Gaming')
    image = models.ImageField(
        upload_to='profile_pics/', null=True, default='profile_pics\_Pure_as_Snow__White_Fashion_Delight_.jpg')
    
    def delete_old_file(self):
        try:
            old_file = CustomUser.objects.get(pk=self.pk).image
            if old_file and default_storage.exists(old_file.path) and old_file != self.image:
                default_storage.delete(old_file.path)
                print(old_file)
        except CustomUser.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        if self.pk:
            self.delete_old_file()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and default_storage.exists(self.image.path):
            default_storage.delete(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        get_latest_by = 'date_of_employment'


class NameList(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=2)

    class Meta:
        ordering = ['name']
        unique_together = ["name", "gender"]


class LastName(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
