from django import template
from django.urls import resolve
from django.db.models.query import QuerySet

register = template.Library()

@register.filter
def absolute_url(value):
    return '/%s' % (resolve(value).route)

@register.filter
def getattr(value, arg):
    return value.__dict__[arg]

@register.filter
def get_list(value, arg):
    return value[arg]

@register.filter
def filter_location(value, arg):
    return value.filter(location=arg)

@register.filter
def exclude_location(value, arg):
    return value.exclude(location=arg)

@register.filter
def slice_from_zero(value, arg):
    return value[0:arg]

@register.filter
def is_query_set(value):
    return isinstance(value, QuerySet)
