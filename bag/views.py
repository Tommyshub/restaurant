from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from menu.models import Product, Category
from profile.models import UserProfile
from decimal import Decimal
from .models import Coupon
from .forms import CouponForm
from bag.contexts import bag_contents


# Shopping Bag
def view_bag(request):
    """ View for displaying the shopping bag """
    return render(request, 'bag/bag.html')


# Adjust shopping bag
def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated{product.name} quantity to {quantity}')
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


def percentage(percent, whole):
    return (percent * whole) / 100


def apply_coupon(request):
    """
    Apply coupon codes to the bag total and give a percentage discount,
    users can use the code how many times they want until it is deactivated.
    """
    form = CouponForm(request.POST)
    if form.is_valid():
        # Discount code from the form
        code = form.cleaned_data['code']
        # Current bag from the context processor
        current_bag = bag_contents(request)
        # Total from the context processor
        total = current_bag['total']
        try:
            # Check if the coupon from the form matches code from the database
            coupon = Coupon.objects.get(code__iexact=code, active=True)
            # If the coupons id is not in the current session, add it.
            request.session['coupon_id'] = coupon.id
            # Calculate the new total after taking away percentage from the coupon
            total_discount = percentage(coupon.discount, total)
            # Subtract the total discount from the total ammount
            new_total = total - total_discount
            # I am trying to update the bag in the session with the new total but I cannot get it to work.
            current_bag['total'] = new_total
            # I assume I have a problem with scope here but I do not understand how to properly update the total in the bag_contents
            bag_contents.total = new_total  # It does not update the total if I try this either
            # The correct values print for both, I cannot see what I am missing.
            print(current_bag['total'])
            print(bag_contents.total)
            messages.success(
                request, f'A discount of  €{total_discount} was applied to you bag and your new total is  €{total}')
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return render(request, 'bag/bag.html', {'form': form})
