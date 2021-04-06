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
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, from_email, ['fluganisoppan@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect("home")

	form = ContactForm()
	return render(request, "contact/contact.html", {'form':form})