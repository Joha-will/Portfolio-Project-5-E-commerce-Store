from django.shortcuts import render, redirect


def view_basket(request):

    """ A view that renders the products in the basket """

    return render(request, "basket/view_basket.html")


def add_to_basket(request, product_id):

    """ A view that give users the ability to add products to basket"""

    product_quantity = int(request.POST.get('quantity'))

    redirect_url = (request.POST.get('redirect_url'))

    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += product_quantity

    else:
        basket[product_id] = product_quantity

    request.session['basket'] = basket

    print(request.session['basket'])

    return redirect(redirect_url)
