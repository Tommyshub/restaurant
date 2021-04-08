from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'contact@tommybratt.se',
                          ['contact@tommybratt.se'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Message successfully sent')
            return redirect("index")

    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})
