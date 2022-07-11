from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import ReplyForm


def blog_overview(request):
    """ View to render blog posts overview """

    posts = BlogPost.objects.all()

    template = 'blog/blog_overview.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def blog_detail(request, blog_id):
    """ View to show a particular blog post """

    queryset = BlogPost.objects
    post = get_object_or_404(queryset, pk=blog_id)
    replies = post.blog_replies.all()

    form = ReplyForm()
    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'replies': replies,
        'form': form,
    }

    return render(request, template, context)
