

class TestCheckoutModels(TestCase):

    def setup(self):
        self.Order1 = Order.objects.create(
            'user_profile': 'tommy',
            'full_name': 'Tommy B'
            'email': 'some@email.com',
            'country': 'germany',
            'phone_number': '34247983743',
            'post_code': '342344',
            'town_or_city': 'Hamburg',
            'street_address1': 'Some adress',
            'street_address2': 'Another adress'
            'county', 'Hamburg',
            'order_number': '786474D080F84C48B8A0102CF385EF0E',
            'date': 'April 10, 2021, 12:16 p.m.',
            'order_total': '6.10',
            'original_bag': '{"1": 1}',
            'stripe_pid': 'pi_1IefjQCdmXI3Hz3AYAAyBYXT',
        )
