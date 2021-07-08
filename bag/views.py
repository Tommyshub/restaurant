from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from menu.models import Product, Category
from profile.models import UserProfile
from decimal import Decimal
from django.conf import settings
from .models import Coupon, UsedCoupon
from .forms import CouponForm
from bag.contexts import bag_contents


@login_required
def view_bag(request):
    """ View for displaying the shopping bag """
    return render(request, 'bag/bag.html')


@login_required
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


@login_required
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
    """ Function for calculating percentage """
    return (percent * whole) / 100


@login_required
def apply_coupon(request):
    """
    Apply coupon codes to the bag total and give a percentage discount,

    """
    form = CouponForm(request.POST)
    if form.is_valid():
        # Discount code from the form
        code = form.cleaned_data['code']
        # Current bag from the context processor
        current_bag = bag_contents(request)
        # Total from the current bag
        total = current_bag['total']
        try:
            # Check if the coupon from the form matches code from the database
            coupon = Coupon.objects.get(code__iexact=code, active=True)
            # Get the used coupons
            is_used = UsedCoupon.objects.filter(
                user=request.user, coupon=coupon).exists()
            # Redirect back to the bag if the coupon is already used
            if is_used:
                messages.error(
                    request, f'Coupon Already Used.')
                return render(request, 'bag/bag.html', {'form': form})
            # Calculate the total discount
            total_discount = percentage(coupon.discount, total)
            # Set total discount in setting
            settings.DISCOUNT = total_discount
            # Calculate new total to show it in message
            new_total = total - total_discount
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
                request, f'''A discount of {coupon.discount}% and total 
                discount of  €{total_discount} was applied to
                you bag and your new total is  €{new_total}''')
        except Coupon.DoesNotExist:
            # Message user about invalid coupon and set coupon id to none
            request.session['coupon_id'] = None
            messages.error(
                request, f'Not a valid coupon code.')
    return render(request, 'bag/bag.html', {'form': form})
