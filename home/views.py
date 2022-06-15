from django.shortcuts import render


# home view adjusted following discussion with mentor
def home(request):
    """ View to render homepage """

    return render(request, 'home/index.html')


# add view to show privacy policy as discussed with mentor
def privacy_policy(request):
    """ View to render privacy policy page """

    return render(request, 'home/privacy_policy.html')
