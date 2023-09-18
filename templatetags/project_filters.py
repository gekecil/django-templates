from django import template

register = template.Library()

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
def get_fields(value):
    return value._meta.get_fields()

@register.filter
def get_field_verbose_name(value, arg):
    return value._meta.get_field(arg).verbose_name

@register.filter
def get_type(value):
    return type(value).__name__
