from django import template

register = template.Library()

def to_and(value):
    # return value[:len(value)-elements]
    return value.replace("is",'ies group')

register.filter('to_and',to_and)
