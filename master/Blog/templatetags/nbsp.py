from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter(name='nbsp2space', is_safe=True)
@stringfilter
def nbsp2space(value):
    return re.sub('&nbsp;', ' ', value, flags=re.IGNORECASE)