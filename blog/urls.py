from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('remove/<pk>/', views.remove_blog_post, name='remove_blog_post'),
]
