from django.test import TestCase, Client
from django.urls import reverse
from checkout.models import Order, OrderLineItem
import json


class TestCheckoutViews(TestCase):

    def setup(self):
        self.client = Client

    def test_checkout_GET(self):

        response = self.client.get(reverse('checkout'))
        # assert that the status code is 302 (found)
        self.assertEqual(response.status_code, 302)
