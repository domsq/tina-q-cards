from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
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

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Action not allowed')
            return redirect(reverse('home'))
        else:
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                reply_form.instance.creator = request.user
                reply = reply_form.save(commit=False)
                reply.post = post
                reply.save()
                messages.success(request, 'Reply successfully added!')
            else:
                messages.error(request, 'Reply not added!')

    form = ReplyForm()
    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'replies': replies,
        'form': form,
    }

    return render(request, template, context)
