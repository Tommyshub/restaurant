from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profile.forms import UserProfileForm
from profile.models import UserProfile
from .forms import OrderForm
from menu.models import Product
from .models import Order, OrderLineItem
from bag.contexts import bag_contents
import stripe
import json


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    # Get public and secret keys for stripe
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        # Get the bag from the session
        current_bag = bag_contents(request)
        # Get the current bag from the context processor
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Get data from the checkout form
        order_form = OrderForm(form_data)
        # Attach the form data to the order form
        if not order_form.is_valid():
            # Display error message if the form is not valid
            messages.error(
                request, 'The form is not valid. Please enter valid data.')
            return redirect(reverse('checkout'))
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # Save the order form without commiting if the form is valid
            pid = request.POST.get('client_secret').split('_secret')[0]
            # Get the payment intent id for stripe
            order.stripe_pid = pid
            # Set the payment intent id for stripe
            order.original_bag = json.dumps(bag)
            # Attach the bag from the session to the order
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # Get the product connected to the item id
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        # Update the order line item and save it
                except Product.DoesNotExist:
                    # Empty the bag if there's a problem
                    if 'bag' in request.session:
                        del request.session['bag']
                    messages.error(request, (
                        """One of the products in your
                        bag wasn't found in our database. "
                        "Please call us for assistance!""")
                    )
                    order.delete()
                    """
                    Update the bag and delete the order if one of the products
                    added does not exist in the database
                    """
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            # Save the information from the form in the session
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment")
            return redirect(reverse('menu'))
        current_bag = bag_contents(request)
        # Get the current bag from the context processor
        total = current_bag['total']
        # Get the total from the current bag
        discount = current_bag['discount']
        # Get the discount from the current bag
        stripe_total = round(total * 100)
        # Calculate the total for stripe
        stripe.api_key = stripe_secret_key
        # Set stripe api key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        # Create payment intent
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
                # Attach the order form to the profile if the user is logged in
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'discount': discount,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle checkout success
    """
    save_info = request.session.get('save_info')
    # Get information to save from the session
    order = get_object_or_404(Order, order_number=order_number)
    # Get the order connected to the order number
    current_bag = bag_contents(request)
    # Get the current bag from the context processor
    discount = current_bag['discount']
    # Get the discount from the current bag
    total = current_bag['total']
    # Get the total from the current bag
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Get the userprofile to connect the order to
        order.user_profile = profile
        # Attach the profile
        order.discount = discount
        # Add the discount
        order.total = total
        # Add the total
        order.save()
        # Save the order
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                # Save the order to the userprofile if save info exists
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']
    # Empty the bag
    request.session['session_coupon'] = 0
    discount = 0
    # Set discount back to zero
    return redirect(reverse('order_history', args=[order_number]))


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Get the payment intent id
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Access the stripe api key
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'save_info': request.POST.get('save_info'),
            'bag': json.dumps(request.session.get('bag', {}))
        })
        # Stripe payment intent data
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed.')
        return HttpResponse(content=e, status=400)
