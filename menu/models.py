import uuid
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField()
    ingredients = models.TextField(max_length=225)
    category = models.ManyToManyField("Category", related_name=("item"))
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # Add checkout button later and handle quantity from checkout basket

    def __str__(self):
        return self.name

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    