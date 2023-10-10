from django.contrib import admin
from .models import *

# Register your models here.


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
