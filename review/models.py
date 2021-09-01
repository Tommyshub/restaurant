from django.db import models
from menu.models import Product
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(1),
                                                        MaxValueValidator(5)])
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
