from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

# Menu
def profile(request):
    """ View for displaying the profile page """
    # Get users profile
    profile = get_object_or_404(UserProfile, user=request.user)
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