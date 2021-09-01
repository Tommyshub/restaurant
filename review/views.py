from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductReviewForm
from .models import ProductReview
from menu.models import Product
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
