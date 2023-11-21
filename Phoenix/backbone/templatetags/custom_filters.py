from django import template
from datetime import date

register = template.Library()

@register.filter(name='calculate_age')
def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


@register.filter(name='cents_to_dollars')
def cents_to_dollars(value):
    """dollars to Ruppes."""
    try:
        return "{:.2f}".format(float(value) / 100)
    except (ValueError, TypeError):
        return value