from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from menu.models import Product
from .forms import TipsForm
from django.contrib.auth.decorators import login_required
from bag.contexts import bag_contents

# Shopping Bag
def view_bag(request):
    """ View for displaying the shopping bag """
    return render(request, 'bag/bag.html')


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {quantity}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def tips(request):
    """
    View to give tips to delivery staff
    """
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = TipsForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            """
            Get the content of the bag and add the 
            tips to the total amount. 
            """
            current_bag = bag_contents(request)
            total = current_bag['total']
            tips = int(request.POST.get('tips'))
            total += tips
            print(total)
            messages.success(request, 
                f'Thank you for giving {tips} euros to our delivery staff')
            return render(request, "index/index.html", {"form": form})
    return render(request, 'bag/bag.html', {'form': form})
