from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductReviewForm
from .models import ProductReview
from menu.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def review(request):
    """ View for displaying the review page """
    reviews = ProductReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'review/review.html', context)


@login_required
def create_review(request, product_name):
    """ View for displaying the create review page """
    product = get_object_or_404(Product, name=product_name)
    reviews = ProductReview.objects.filter(user=request.user, product=product)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.comment = request.POST['comment']
            review.rating = request.POST['rating']
            review.user = request.user
            if not reviews:
                review.save()
                messages.success(
                    request, f'Review for {product} successfully posted !')
            else:
                messages.error(
                    request, f'You cannot review {product} twice!')
            return redirect('profile')
        else:
            messages.error(
                request, f'Error creating review for {product}')
    form = ProductReviewForm(request.POST or None)
    context = {
        'form': form,
        'product_name': product_name,
    }
    return render(request, 'review/create_review.html', context)


@login_required
def edit_review(request, product_name):
    """ Edit Review """
    product = get_object_or_404(Product, name=product_name)
    review = get_object_or_404(ProductReview, product=product)
    form = ProductReviewForm(instance=review)
    # Populate the form with the data from the review instance
    if request.method == 'POST' and request.user.is_superuser:
        form = ProductReviewForm(request.POST, instance=review)
        # Get the new form data
        if form.has_changed and form.is_valid():
            try:
                review = form.save()
                # Save the new form data to the original review
                messages.success(
                    request, f'Successfully edited {product.name}')
                return redirect('review')
            except Exception as e:
                messages.error(request, f'Error editing review: {e}')
            return redirect('review')
        else:
            messages.error(request, 'Error editing review!')
    template = 'review/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product_name': product_name,
    }

    return render(request, template, context)


@login_required
def remove_review(request, product_name):
    """Remove Review """
    product = get_object_or_404(Product, name=product_name)
    # Access the review form
    form = ProductReviewForm(request.POST or None)
    if request.method == 'POST':
        try:
            # Access the review
            review = get_object_or_404(ProductReview, product=product)
            # Delete the review
            review.delete()
            messages.success(
                request, f'Removed review for {product_name}')
            return redirect('review')
        except Exception as e:
            messages.error(request, f'Error removing review: {e}')
            return HttpResponse(status=500)
    context = {
        'form': form,
        'product_name': product_name,
    }

    return render(request, 'review/review.html', context)
