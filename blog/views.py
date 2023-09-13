from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    # context = {'title':'bitcoin crashed again!', 
    #             'content':'bitcoin was flying but now grounded as allways', 
    #             'author': 'Hesan Adeli'}
    # return render(request, 'blog/blog-single.html', context)
    
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid, status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    # posts = Post.objects.filter(status=0)
    # posts = Post.objects.all()
    # posts = Post.objects.get(id=pid)
    posts = get_object_or_404(Post, pk=pid)
    context = {'post':posts}
    return render(request, 'test.html', context) 