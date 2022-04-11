from django import template

register = template.Library()


def rem(value, args):
    if type(value)==str:
        return value.replace(args, "")
    return value.name.replace(args, "")

register.filter('rem', rem)