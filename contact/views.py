from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form = ContactForm(request.POST)
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
