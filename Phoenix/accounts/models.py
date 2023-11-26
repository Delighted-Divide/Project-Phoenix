from typing import Any
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.files.storage import default_storage
from django.core.validators import MinValueValidator, MaxValueValidator

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
    nationality = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=50, choices=[
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Other', 'Other'),
    ], blank=True)
    hobby = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='profile_pics/', null=True, default='profile_pics\_Pure_as_Snow__White_Fashion_Delight_.jpg')
    color_index = models.IntegerField(default=1, editable=False)
    color2_index = models.IntegerField(default=2, editable=False)
    
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

class Symptom(models.Model):
    name = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255, verbose_name='Recommended Specialist')

    def __str__(self):
        return self.name
    


class Diagnosis(models.Model):
    name = models.CharField(max_length=255)
    recommended_specialist = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class PhysicalExaminationResponse(models.Model):
    RESPONSE_TYPES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]

    response = models.TextField()
    response_type = models.CharField(max_length=8, choices=RESPONSE_TYPES)

    def __str__(self):
        return f"{self.response_type}: {self.response[:50]}..."


class Allergy(models.Model):
    type = models.CharField(max_length=255)  # You can adjust the default type as needed

    def __str__(self):
        return self.type



class ElectricityBill(models.Model):
    date_issued = models.DateField(unique=True)
    total_kwh = models.FloatField()  # Total kilowatt-hours used
    cost_per_kwh = models.FloatField()  # Cost per kilowatt-hour
    total_cost = models.FloatField()  # Total cost of the bill

    def __str__(self):
        return f"Electricity Bill - {self.date_issued} - ${self.total_cost}"

class WaterBill(models.Model):
    date_issued = models.DateField(unique=True)
    total_liters = models.FloatField()  # Total liters used
    cost_per_liter = models.FloatField()  # Cost per liter
    total_cost = models.FloatField()  # Total cost of the bill

    def __str__(self):
        return f"Water Bill - {self.date_issued} - ${self.total_cost}"
    




class HospitalStaff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')
    ])
    birthday = models.DateField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_employment = models.DateField(auto_now_add=True)
    nationality = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=50, choices=[
        ('Single', 'Single'), ('Married', 'Married'), 
        ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), 
        ('Other', 'Other')
    ])
    job_role = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_role}"
    



class Medicine(models.Model):
    name = models.CharField(max_length=500, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prescription_required = models.BooleanField(default=False)
    package = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=100)
    composition = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
