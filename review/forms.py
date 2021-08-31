from django import forms


class ProductReviewForm(forms.ModelForm):
    class Meta:
        fields = ['comment', 'rating']
