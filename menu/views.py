from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product, Category


# Menu
def menu(request, *args, **kwargs):
    """ View for displaying the menu page """
    # get every item from each category
    bowls = Product.objects.filter(category__name__contains='Bowls')
    burgers = Product.objects.filter(category__name__contains='Burgers')
    drinks = Product.objects.filter(category__name__contains='Drinks')
    pizzas = Product.objects.filter(category__name__contains='Pizzas')
    desserts = Product.objects.filter(category__name__contains='Desserts')

    # pass into context
    context = {
        'bowls': bowls,
        'burgers': burgers,
        'pizzas': pizzas,
        'drinks': drinks,
        'desserts': desserts,
    }
    # render the template
    return render(request, 'menu/menu.html', context)


@login_required
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    add = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += add
        messages.success(request, f'Added {product.name} to your bag')
    else:
        bag[item_id] = add
        messages.success(request, f'Added {product.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)
