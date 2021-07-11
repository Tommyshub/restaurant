from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
