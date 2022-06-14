from django.shortcuts import render
from .models import BlogPost


def view_blog(request):
    """ View to render blog posts """

    posts = BlogPost.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
