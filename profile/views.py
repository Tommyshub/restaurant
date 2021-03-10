from django.shortcuts import render

# Menu
def profile(request):
    """ View for displaying the profile page """
    return render(request, 'profile/profile.html')