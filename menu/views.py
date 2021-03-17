from django.shortcuts import render
from django.views import View
from .models import MenuItem, Category

# Menu
def menu(request, *args, **kwargs):
    """ View for displaying the menu page """
    # get every item from each category
    bowls = MenuItem.objects.filter(category__name__contains='bowls')
    burgers = MenuItem.objects.filter(category__name__contains='burgers')
    drinks = MenuItem.objects.filter(category__name__contains='Drinks')
    pizzas = MenuItem.objects.filter(category__name__contains='Pizzas')
    desserts = MenuItem.objects.filter(category__name__contains='Desserts')

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
