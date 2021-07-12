from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form = ContactForm(request.POST)
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
