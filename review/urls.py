from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('create_review/<product_name>',
         views.create_review, name='create_review'),
    path('edit_review/<product_name>', views.edit_review, name='edit_review'),
    path('remove_review/<product_name>',
         views.remove_review, name='remove_review'),
]
