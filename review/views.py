from django.shortcuts import render
from django.contrib import messages
from .forms import ProductReviewForm


def review(request):
    """ View for displaying the review page """
    return render(request, 'review/review.html')


def create_review(request, product_name):
    """ View for displaying the create review page """
    if request.method == 'POST' and user.is_authenticated:
        form = ProductReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product_name
            review.comment = request.POST['comment']
            review.rating = request.POST['rating']
            review.user = request.user
            review.save()
            messages.success(
                request, f'Successfully created review for {review.product}')
        else:
            messages.error(
                request, f'Error creating review for {review.product}')
    form = ProductReviewForm(request.POST or None)
    context = {
        'form': form,
        'product_name': product_name,
    }
    return render(request, 'review/create_review.html', context)
