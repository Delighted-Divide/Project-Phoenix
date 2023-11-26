# serializers.py in your Django app directory
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email',
            'address', 'phone_number', 'gender', 'birthday', 'city',
            'country', 'date_of_employment', 'nationality', 'language',
            'marital_status', 'hobby', 'image', 'color_index', 'color2_index'
        ]
