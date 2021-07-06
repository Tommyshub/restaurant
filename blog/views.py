from django.shortcuts import render
from .models import BlogPost

# Index


def blog(request):
    """ View for displaying the blog page """
    posts = BlogPost.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})
