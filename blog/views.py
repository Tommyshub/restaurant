from django.shortcuts import render
from .models import BlogPost
from .forms import BlogForm

# Index


def blog(request):
    """ View for displaying the blog page """
    posts = BlogPost.objects.all()
    form = BlogForm()
    context = {'form': form, 'posts': posts}
    return render(request, "blog/blog.html", context)
