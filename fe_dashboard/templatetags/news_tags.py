import random

from django import template

register = template.Library()


@register.inclusion_tag('fe_dashboard/_news.html')
def news_avatar(news):
    return {'news': news, 'num': random.randint(0, 215)}

