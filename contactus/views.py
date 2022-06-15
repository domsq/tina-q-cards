from django.shortcuts import render
from .forms import ContactForm


def contact_us(request):
    """
    Display the contact us form and handle submission
    """

    form = ContactForm()

    template = 'contactus/contactus.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
