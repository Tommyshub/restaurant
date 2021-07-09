from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    name = forms.CharField(required=True)
    email = forms.EmailField(validators=[validate_email], required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
