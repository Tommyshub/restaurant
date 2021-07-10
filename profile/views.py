from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Menu
@login_required
def profile(request):
    """ View for displaying the profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    # Get users profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        # Get the form instance for the profile connected to the user
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    # Get all order connected to the user
    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    # Get the order connected to the order number
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    # Put that order into context for rendering of the template
    return render(request, template, context)
