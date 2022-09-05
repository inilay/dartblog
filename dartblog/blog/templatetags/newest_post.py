from django import template
from django.core.cache import cache

from blog.models import Post


register = template.Library()

@register.inclusion_tag('blog/new_post.html')
def show_new_post(post_type='menu'):
    post = cache.get_or_set('new_post', Post.objects.order_by('-created_at').first(), 30)
    #categories = Category.objects.all()
    return {'post': post}
