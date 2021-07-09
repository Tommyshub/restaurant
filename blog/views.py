from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm
from django.http import HttpResponse, HttpResponseRedirect


def blog(request):
    """ View for displaying the blog page """
    posts = BlogPost.objects.all()
    # Get all posts to show when rendering the template
    form = BlogForm(request.POST or None)
    # Access the blog form
    context = {'form': form, 'posts': posts}
    # Context for rendering template
    if request.method == 'POST':
        if request.user.is_superuser:
            title = request.POST.get('title')
            image = request.FILES.get('image')
            body = request.POST.get('body')
            # Access the title, image and body from the form
            blog = BlogPost.objects.create(
                title=title,
                image=image,
                body=body,
            )
            # Create a new blog post object with the data from the form
            blog.save()
            # Save blog post
            messages.success(request, 'Blog successfully posted!')
            return HttpResponseRedirect('')
        else:
            messages.error(
                request, 'Form is not valid!')
    return render(request, "blog/blog.html", context)


@login_required
def remove_blog_post(request, item_id):
    """Remove blog post"""
    posts = BlogPost.objects.all()
    # Get all posts to show when rendering the template
    form = BlogForm(request.POST or None)
    # Access the blog form
    context = {'form': form, 'posts': posts}
    # Context for rendering template
    if request.method == 'POST' and request.user.is_superuser:
        try:
            post = get_object_or_404(BlogPost, pk=item_id)
            # Access the blog post related to the id in the template
            image = post.image
            # Access the image for the blog post
            image.delete()
            # Delete the image
            post.delete()
            # Delete the post
            messages.success(
                request, f'Removed {post.title}')
            return HttpResponseRedirect('')
        except Exception as e:
            messages.error(request, f'Error removing post: {e}')
            return HttpResponse(status=500)
    return render(request, 'blog/blog.html', context)


@login_required
def edit_blog_post(request, item_id):
    """ Edit blog post """
    post = get_object_or_404(BlogPost, pk=item_id)
    # Get the current blog post
    form = BlogForm(instance=post)
    # Populate the form with the data from the post instance
    if request.method == 'POST' and request.user.is_superuser:
        form = BlogForm(request.POST, request.FILES, instance=post)
        # Get the new form data
        if form.has_changed and form.is_valid():
            try:
                post = form.save()
                # Save the new form data to the original post
                messages.success(
                    request, f'Successfully edited {post.title}')
                return redirect(reverse('blog'))
            except Exception as e:
                messages.error(request, f'Error editing blog post: {e}')
                return HttpResponse(status=500)
        else:
            messages.error(request, 'Error editing blog post!')
    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)
