import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from menu.models import Product
from profile.models import UserProfile
from django.core.validators import validate_email
from profile.validators import (validate_phone_number, validate_postal_code,
                                validate_county, validate_city,
                                validate_alpha_numeric, validate_name)


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(
        validators=[validate_name], max_length=50, null=False, blank=False)
    email = models.EmailField(
        validators=[validate_email], max_length=254, null=False, blank=False)
    phone_number = models.CharField(validators=[validate_phone_number],
                                    max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(
        validators=[validate_postal_code], max_length=20,
        null=True, blank=True)
    town_or_city = models.CharField(
        validators=[validate_city], max_length=40, null=False, blank=False)
    street_address1 = models.CharField(
        validators=[validate_alpha_numeric],
        max_length=80, null=False, blank=False)
    street_address2 = models.CharField(
        validators=[validate_alpha_numeric],
        max_length=80, null=True, blank=True)
    county = models.CharField(
        validators=[validate_county], max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a unique order number using uuid
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the total everytime a item is added.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))[
            'lineitem_total__sum'] or 0
        self.total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method in order to set the order number
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name="lineitems")
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method in order to set the order number
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order.order_number
