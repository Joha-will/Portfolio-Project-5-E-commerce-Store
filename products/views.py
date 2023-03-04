from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib import messages

from django.db.models import Q

from .models import Product, Category


def all_products(request):
    """ A view that displays all product to customers"""

    products = Product.objects.all()

    query = None

    if request.GET:

        if 'q' in request.GET:

            query = request.GET['q']

            if not query:
                messages.error(request, "You did not enter a search!!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)

            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, "products/products.html", context)


def all_categories(request):

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return context


def product_detail(request, slug):
    """ A view that displays all product to customers"""

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)
