from django import template

register = template.Library()


# Create your views here.

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='simple') 
def simple(key):
    return key

@register.filter(name='def_type') 
def def_type(key):
    return type(key)

@register.simple_tag
def dict_convert(dictesh,key):
    return dictesh[key]