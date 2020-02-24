from django.template import Library
from django.utils.encoding import force_text

register = Library()


def force_text_filter(obj):
    return force_text(obj)


register.filter('force_text', force_text_filter)
