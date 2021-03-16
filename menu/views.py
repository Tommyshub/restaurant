from django.shortcuts import render

# Menu
def menu(request):
    """ View for displaying the menu page """
    def get(self, request, *args, **kwargs):
        # get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='Appetizers')
        drinks = MenuItem.objects.filter(category__name__contains='Drinks')
        entrees = MenuItem.objects.filter(category__name__contains='Entrees')
        desserts = MenuItem.objects.filter(category__name__contains='Desserts')
        
        # pass into context
        context = {
            'appetizers': appetizers,
            'drinks': drinks,
            'entrees': entrees,
            'desserts': desserts,
        }
    # render the template
    return render(request, 'menu/menu.html', context)
        
        