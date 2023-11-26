from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from .models import *

# Register your models here.


class CustomUserAdmin(UserAdmin):
    def custom_delete_users(modeladmin, request, queryset):
        for user in queryset:
            # Custom delete logic for users
            user.delete()
            messages.success(request, f"User {user.username} was successfully deleted.")

    model = CustomUser
    actions = [custom_delete_users]
    list_display = ['username', 'first_name', 'last_name', 'email',
                    'phone_number', 'gender', 'birthday', 'city', 'country']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'address', 'phone_number',
         'gender', 'birthday', 'city', 'country','nationality','language','hobby','marital_status', 'image')}),
    )

    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(NameList)
admin.site.register(LastName)
admin.site.register(Allergy)
admin.site.register(Symptom)
admin.site.register(Diagnosis)
admin.site.register(PhysicalExaminationResponse)
admin.site.register(ElectricityBill)
admin.site.register(WaterBill)
admin.site.register(HospitalStaff)

