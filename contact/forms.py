from django import forms
from django.forms import ModelForm, Textarea
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'subject',
            'first_name', 
            'last_name', 
            'email',
            'message',
        )