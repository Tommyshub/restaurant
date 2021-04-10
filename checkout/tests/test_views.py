from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Order, OrderLineItem
import json


class TestCheckoutViews(TestCase):

    def setup(self):
        self.client = Client
        self.checkout_url = reverse('checkout')

    def test_checkout_GET(self):

        response = self.client.get(reverse(self.checkout_url))
        # assert that the status code is 302 (found)
        self.assertEqual(response.status_code, 302)
