from django import template
from datetime import date

register = template.Library()

@register.filter(name='calculate_age')
def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
