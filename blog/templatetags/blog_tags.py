from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now()).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    return posts

@register.filter
def snippet(value, arg=20):
    return value[:arg] + ' ...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now()).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

