from django import forms
from .models import BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'image', 'body')

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise forms.ValidationError('Fields cannot be empty.')
        return super().clean(*args, **kwargs)
