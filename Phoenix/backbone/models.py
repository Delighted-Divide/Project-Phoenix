from collections.abc import Iterable
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(
        'accounts.CustomUser', on_delete=models.CASCADE, related_name='doctor_profile')
    # specialization = models.ManyToManyField('Specialization')
    # sub_specialization = models.ManyToManyField(
    #     'SubSpecialization', blank=True)
    years_of_experience = models.PositiveIntegerField(blank=True)
    degrees = models.ManyToManyField('degree')
    speciality = models.ForeignKey(
        'specialist', on_delete=models.CASCADE, related_name='doctors')
    subspecialities = models.ManyToManyField(
        'specialist', blank=True, related_name='doctors_subspecialities')
    certifications = models.PositiveIntegerField(default=0,
                                                 help_text="Number of certifications")

    # Professional Achievements
    publications_count = models.PositiveIntegerField(default=0)
    awards_count = models.PositiveIntegerField(default=0)
    conferences_attended_count = models.PositiveIntegerField(default=0)
    seminars_attended_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        user = str(self.user).title()
        return f"Dr. {user}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        get_latest_by = 'user__date_of_employment'


class Degree(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Specialist(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.name}"
