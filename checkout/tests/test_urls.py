from django.test import SimpleTestCase
from django.urls import resolve, reverse
from checkout.views import checkout, checkout_success, cache_checkout_data


class TestCheckoutUrls(SimpleTestCase):
    # Check that the the view resolves to the right urls
    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    # Added args as order number
    def test_checkout_success_url_is_resolved(self):
        url = reverse('checkout_success', args=['23432423432432'])
        self.assertEquals(resolve(url).func, checkout_success)

    def test_cache_checkout_data_url_is_resolved(self):
        url = reverse('cache_checkout_data')
        self.assertEquals(resolve(url).func, cache_checkout_data)
