from django.shortcuts import render
from .models import WelcomeMessage


def home(request):
    """ View to render homepage """

    messages = WelcomeMessage.objects.all()

    context = {
        'messages': messages,
    }

    return render(request, 'home/index.html', context)
