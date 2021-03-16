from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    friendly_name = models.SlugField()
    ingredients = models.TextField(max_length=225, null=True, blank=True)
    category = models.ManyToManyField("Category", related_name=("item"))
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # Add checkout button later and handle quantity from checkout basket

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name