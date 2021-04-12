from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tips(models.Model):
    tips = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Coupon(models.Model):
    code = models.CharField(max_length=8, unique=True)
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
