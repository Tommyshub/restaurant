from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Menu
def profile(request):
    """ View for displaying the profile page """
    # Get users profile
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
    # Form for the user profile
    form = UserProfileForm(request.POST, instance=profile)
    # Get order history
    orders = profile.orders.all()
    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past order confirmation for order {order_number} '
        f'A confirmation email was sent to {order.email} on {order.date}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
