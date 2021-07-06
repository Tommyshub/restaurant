from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not validate_email(email):
            raise forms.ValidationError("Invalid email")
        return email
