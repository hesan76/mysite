from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now()).order_by('-published_date')

    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1) 

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):    
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    post = get_object_or_404(posts, pk=pid)
    post.increase_view()
    context = {'post':post, 
               'next':posts.filter(id__gt=post.id).order_by('id').first(),
               'previous':posts.filter(id__lt=post.id).order_by('-id').first()}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test(request):
    # posts = Post.objects.filter(status=0)
    # posts = Post.objects.all()
    # posts = Post.objects.get(id=pid)
    # posts = get_object_or_404(Post, pk=pid)
    # context = {'post':posts}
    return render(request, 'test.html') 