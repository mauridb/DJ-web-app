import random

from django import template

register = template.Library()


@register.inclusion_tag('fe_dashboard/_lecture.html')
def lecture_avatar(lecture):
    return {'lecture': lecture, 'num': random.randint(0, 215)}

