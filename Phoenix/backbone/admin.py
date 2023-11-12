from typing import Any
from django.contrib import admin
from .models import *
from django import forms

# Register your models here.


# class PatientTestAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         scan_test_choices = [(ContentType.objects.get_for_model(
#             ScanTest).pk, obj) for obj in ScanTest.objects.all()]
#         lab_test_choices = [(ContentType.objects.get_for_model(
#             LabTest).pk, obj) for obj in LabTest.objects.all()]
#         self.fields['content_type'].choices = scan_test_choices + \
#             lab_test_choices


# class PatientTestAdmin(admin.ModelAdmin):
#     form = PatientTestAdminForm


admin.site.register(Doctor)
admin.site.register(Degree)
admin.site.register(Specialist)
admin.site.register(Patient)
admin.site.register(OutpatientVisit)
admin.site.register(Room)
admin.site.register(Bed)
admin.site.register(InpatientVisit)
admin.site.register(Lab)
admin.site.register(LabTest)
admin.site.register(ScanTest)
admin.site.register(PatientTest)
admin.site.register(Customer)
admin.site.register(DoctorWorkShift)
admin.site.register(DoctorVisit)

