from django import template

register = template.Library()

class Scheme(template.Node):
    def render(self, context):
        return context['request'].scheme

class Host(template.Node):
    def render(self, context):
        return context['request'].getHost()

class Port(template.Node):
    def render(self, context):
        return context['request'].getPort()

class BaseUri(template.Node):
    def render(self, context):
        return context['request'].build_absolute_uri('/')

@register.tag
def scheme(parser, token):
    return Scheme()

@register.tag
def host(parser, token):
    return Host()

@register.tag
def port(parser, token):
    return Port()

@register.tag
def base_uri(parser, token):
    return BaseUri()
