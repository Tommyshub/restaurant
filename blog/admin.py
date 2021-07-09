from django.contrib import admin
from .models import BlogPost
from .forms import BlogForm


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image', 'id']
    form = BlogForm


admin.site.register(BlogPost, BlogAdmin)
