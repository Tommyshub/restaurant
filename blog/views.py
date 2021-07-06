from django.shortcuts import render


# Index
def blog(request):
    """ View for displaying the blog page """
    posts = BlogPost.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})
