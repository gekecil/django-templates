from django import template
from django.urls import resolve
from django.db.models.query import QuerySet

register = template.Library()

@register.filter
def full_url_name(value):
    url = resolve(value)

    return '%s:%s' % (url.namespace, url.url_name)

@register.filter
def url_id(value):
    view, args, kwargs = resolve(value)

    try:
        return kwargs['id']

    except:
        return None

@register.filter
def has_attribute(value, arg):
    return hasattr(value, arg)

@register.filter
def get_attribute(value, arg):
    try:
        return value.__getattribute__(arg)

    except AttributeError:
        return value.__dict__.get(arg)

    except:
        return None

@register.filter
def get_list(value, arg):
    return value[arg]

@register.filter
def to_string(value):
    return value.__dict__

@register.filter
def get_fields(value):
    return value._meta.get_fields()

@register.filter
def get_field_verbose_name(value, arg):
    return value._meta.get_field(arg).verbose_name

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

@register.filter
def is_equal(value, arg):
    return value == arg
