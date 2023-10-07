from django.contrib import admin
from .models import Doctor, Degree, Specialist

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Degree)
admin.site.register(Specialist)
