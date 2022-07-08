from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Product
from .forms import ProductForm


def all_products(request):
    """
    View to show all products, including
    sorting and searching queries
    """

    categories = None
    direction = None
    products = Product.objects.all()
    query = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You entered no search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def add_product(request):
    """ Add a new product """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
