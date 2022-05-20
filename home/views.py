from django.shortcuts import render


def home(request):
    """ View to render homepage """

    return render(request, 'base.html')
