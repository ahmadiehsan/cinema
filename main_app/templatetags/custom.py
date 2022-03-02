from django import template
from django.conf import settings
from django.utils.translation import gettext as _

register = template.Library()


@register.filter
def bootstrap_level_tag_map(value):
    bootstrap_level_tags = {
        'debug': 'dark',
        'info': 'info',
        'success': 'success',
        'warning': 'warning',
        'error': 'danger',
    }
    return bootstrap_level_tags[value]


@register.filter
def room_color_map(value):
    room_colors = {
        'R': 'danger',
        'B': 'primary',
        'G': 'success',
        'Y': 'warning',
    }
    return room_colors[value]


@register.filter
def summary(text, length=50):
    if not text:
        return _('Without text')

    if len(text) > length:
        return f'{text[:length]}...'
    else:
        return text


@register.filter
def multiply(number, multiply_to):
    return int(number) * multiply_to


@register.filter
def subtract(number, subtract_by):
    return int(number) - subtract_by


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, '')
