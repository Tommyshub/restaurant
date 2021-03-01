from django.shortcuts import render

# Create your views here.
def index(request):
    """ View for displaying the index pag """
    return render(request, 'index/index.html')
