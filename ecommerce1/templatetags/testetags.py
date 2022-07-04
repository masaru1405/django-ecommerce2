from django import template

register = template.Library()

@register.filter
def cut(value, arg):
   return value.replace(arg, '')

@register.filter
def lower(value):
   return value.lower()

@register.simple_tag
def current_timer(format_string):
   return datetime.datetime.now().strftime(format_string)