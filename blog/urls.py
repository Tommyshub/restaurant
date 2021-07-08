from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('remove/<item_id>/', views.remove_blog_post, name='remove_blog_post'),
    path('edit/<int:item_id>', views.edit_blog_post, name='edit_blog_post'),
]
