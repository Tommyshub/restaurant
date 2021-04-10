from django.test import SimpleTestCase
from checkout.forms import OrderForm


class TestCheckoutForm(SimpleTestCase):

    # Test that forms is not valid if 6 required fields are not present
    def test_order_form_no_data(self):
        form = OrderForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 6)
