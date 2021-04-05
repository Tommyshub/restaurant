from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'subject',
            'first_name', 
            'last_name', 
            'email', 
        )

        widgets = {
                'message': Textarea(attrs={'cols': 80, 'rows': 20}),
            }