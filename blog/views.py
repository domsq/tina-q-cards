from django.shortcuts import render
from .models import BlogPost, Reply


def blog_overview(request):
    """ View to render blog posts """

    posts = BlogPost.objects.all()

    template = 'blog/blog_overview.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
