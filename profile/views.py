from django.shortcuts import render

# Menu
def profile(request):
    """ View for displaying the profile page """
    template = 'profile/profile.html'
    context = {}
    
    return render(request, template, context, 'profile/profile.html')