from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email',
                    'phone_number', 'gender', 'birthday', 'city', 'country']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'address', 'phone_number',
         'gender', 'birthday', 'city', 'country', 'image')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
