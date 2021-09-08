from django.shortcuts import render, redirect, reverse, get_object_or_404
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
    template = 'profile/profile.html'
    # Get users profile
    print(request.session)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        # Get all order connected to the user
        orders = profile.orders.all()
        context = {
            'form': form,
            'orders': orders,
        }
        # Get the form instance for the profile connected to the user
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
        else:
            messages.error(request, 'Profile could not be updated')
        return render(request, template, context)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    # Get the order connected to the order number
    order = get_object_or_404(Order, order_number=order_number)
    # Check if the email of the order is the same as the current users email
    if request.user.email == order.email:
        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }
    else:
        messages.error(request, 'You are not allowed to view this order.')
        return redirect(reverse('profile'))
    return render(request, template, context)
