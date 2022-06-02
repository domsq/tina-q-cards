from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    View to show all products, including
    sorting and searching queries
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You entered no search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    View to show product detail
    """

    queryset = Product.objects
    product = get_object_or_404(queryset, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
