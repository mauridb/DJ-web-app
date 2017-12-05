import random

from django import template

register = template.Library()


@register.inclusion_tag('fe_dashboard/_course.html')
def course_avatar(course):
    return {'course': course, 'num': random.randint(0, 215)}

