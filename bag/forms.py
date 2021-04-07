from django import forms 
from .models import Tips


class TipsForm(forms.ModelForm):
    class Meta:
        model = Tips
        fields = ['tips',]
