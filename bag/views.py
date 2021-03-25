from django.shortcuts import render, redirect

# Shopping Bag
def view_bag(request):
    """ View for displaying the shopping bag """
    return render(request, 'bag/bag.html')