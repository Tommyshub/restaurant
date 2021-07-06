from django.shortcuts import render


# Index
def blog(request):
    """ View for displaying the index page """
    return render(request, 'blog/blog.html')
