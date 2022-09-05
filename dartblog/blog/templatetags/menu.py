from django import template
from django.core.cache import cache

from blog.models import Category
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = cache.get_or_set('cat', Category.objects.alias(cnt=Count('posts')).filter(cnt__gt=0), 30)
    #categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}
