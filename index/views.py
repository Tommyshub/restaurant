from django.shortcuts import render


# Index
def index(request):
    """ View for displaying the index page """
    return render(request, 'index/index.html')
