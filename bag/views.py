from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from menu.models import Product
from .models import Coupon, UsedCoupon
from .forms import CouponForm


@login_required
def view_bag(request):
    """ View for displaying the shopping bag """
    return render(request, 'bag/bag.html')


@login_required
def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    # Get the product connected to the item id
    quantity = int(request.POST.get('quantity'))
    # Get the quantity from the session
    bag = request.session.get('bag', {})
    # Get the bag from the session
    if quantity > 0:
        bag[item_id] = quantity
        # Add the quantity to the bag item if items are greater than 0
        messages.success(
            request, f'Updated{product.name} quantity to {quantity}')
    else:
        # Otherwise remove the item completely
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
    # Set the bag in the session to the updated bag
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


@login_required
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        # Get the product connected to the item id
        bag = request.session.get('bag', {})
        # Get the bag from the session
        bag.pop(item_id)
        # Pop the item_id (product) from the bag
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@login_required
def apply_coupon(request):
    """
    Apply coupon codes to the bag total and give a percentage discount,

    """
    form = CouponForm(request.POST)
    if form.is_valid():
        # Discount code from the form
        code = form.cleaned_data['code']
        try:
            # Check if the coupon from the form matches code from the database
            coupon = Coupon.objects.get(code__iexact=code, active=True)
            # Get the used coupons
            is_used = UsedCoupon.objects.filter(
                user=request.user, coupon=coupon).exists()
            # Redirect back to the bag if the coupon is already used
            if is_used:
                messages.error(
                    request, f'The code {coupon.code} was already used.')
                return render(request, 'bag/bag.html', {'form': form})
            # Put the coupon code in the session
            request.session['session_coupon'] = coupon.discount
            # Keep track and save used coupons
            used_coupon = UsedCoupon()
            # Attach current user to the used coupon
            used_coupon.user = request.user
            # Set which coupon is used
            used_coupon.coupon = coupon
            # Save the used coupon
            used_coupon.save()
            # Message the user about the applied discount
            messages.success(
                request, f'''A discount of {coupon.discount}% was applied to
                you bag!''')
        except Coupon.DoesNotExist:
            # Message user about invalid coupon and set coupon id to none
            request.session['coupon_id'] = None
            messages.error(
                request, f'This is not valid coupon code!')
    return render(request, 'bag/bag.html', {'form': form})
