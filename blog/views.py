from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
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


def remove_blog_post(request, item_id):
    """ Remove blog post """
    form = BlogForm(request.POST or None)
    if request.method == 'POST' and request.user.is_superuser:
        try:
            post = get_object_or_404(BlogPost, id=item_id)
            image = post.image
            messages.success(
                request, f'Removed {post.title}')
            image.delete()
            post.delete()
            return HttpResponseRedirect('')
        except Exception as e:
            messages.error(request, f'Error removing post: {e}')
            return HttpResponse(status=500)
    return render(request, 'blog/blog.html', {'form': form})


def edit_blog_post(request, item_id):
    """ Edit blog post """
    post = get_object_or_404(BlogPost, pk=item_id)
    form = BlogForm(instance=post)
    if request.method == 'POST' and request.user.is_superuser:
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.has_changed and form.is_valid():
            try:
                post = form.save()
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
