from django.template.defaultfilters import register
from django import template
register = template.Library()
@register.filter
def times(number):
    return range(number)
