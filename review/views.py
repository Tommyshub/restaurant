from django.shortcuts import render


def review(request):
    """ View for displaying the review page """
    return render(request, 'review/review.html')


def create_review(request):
    """ View for displaying the create review page """
    return render(request, 'review/create_review.html')
