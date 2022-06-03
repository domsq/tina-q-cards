from django.shortcuts import render


def view_basket(request):
    """ A view to render the basket contents """

    return render(request, 'basket/basket.html')
