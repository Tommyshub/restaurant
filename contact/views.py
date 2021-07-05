from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Message successfully sent')
        else:
            messages.error(request, 'Message could not be sent')
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
