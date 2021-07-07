from django.shortcuts import render
from django.contrib import messages
from .models import BlogPost
from .forms import BlogForm
from django.http import HttpResponse, HttpResponseRedirect


def blog(request):
    """ View for displaying the blog page """
    posts = BlogPost.objects.all()
    form = BlogForm(request.POST or None)
    context = {'form': form, 'posts': posts}
    if request.method == 'POST':
        if request.user.is_superuser:
            title = request.POST.get('title')
            image = request.FILES.get('image')
            body = request.POST.get('body')
            blog = BlogPost.objects.create(
                title=title,
                image=image,
                body=body,
            )
            blog.save()
            messages.success(request, 'Blog successfully posted!')
            return HttpResponseRedirect('')
        else:
            messages.error(
                request, 'Form is not valid!')

    return render(request, "blog/blog.html", context)
