from django.shortcuts import render

# Menu
def contact(request):
    """ View for displaying the menu page """
    return render(request, 'contact/contact.html')