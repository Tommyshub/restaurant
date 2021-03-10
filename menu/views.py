from django.shortcuts import render

# Menu
def menu(request):
    """ View for displaying the menu page """
    return render(request, 'menu/menu.html')