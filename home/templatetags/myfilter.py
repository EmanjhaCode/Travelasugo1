from django import template
import ast
register = template.Library()

def replace_comma(value):
    # return value[:len(value)-elements]
    return value.split(',')[0]

register.filter('replace_comma',replace_comma)

def string_to_list(data):
    return data.strip('][').split(', ')

register.filter('string_to_list',string_to_list)

def remove_quote(data1):
    return data1.replace("'", '')

register.filter('remove_quote',remove_quote)

def remove_back_slash(data1):
    return data1.replace("\\", '')

register.filter('remove_back_slash',remove_back_slash)


def string_to_dict(data):
    return ast.literal_eval(data)

register.filter('string_to_dict',string_to_dict)

def convert_byte_to_string(value):
    value = value.decode('ascii')
    return value.decode("utf-8")

register.filter('convert_byte_to_string',string_to_dict)

def replace_blank_with_plus(data1):
    return data1.replace(" ", '+')

register.filter('replace_blank_plus',replace_blank_with_plus)

def change_color(data1):
    data = data1.lower()
    return data.replace("phone", '<b style="color:red;">Phone</b>')

register.filter('change_color',change_color)
