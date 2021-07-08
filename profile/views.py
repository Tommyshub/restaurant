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
    # Get users profile
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
    # Form for the user profile
    form = UserProfileForm(instance=profile)
    # Get order history
    orders = profile.orders.all()
    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
