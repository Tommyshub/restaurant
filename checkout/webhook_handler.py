from django.http import HttpResponse
from .models import Order, OrderLineItem
from menu.models import Product
import json
import time


class StripeWH_Handler:
    """ Handles stripe webhooks """
    
    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        Handle generic / unknown or unexpected webhook events 
        """
        return HttpResponse(
            content = f'Unhandled webhook received: {event["type"]}',
            status = 200)


    def handle_payment_intent_succeeded(self, event):
        """
        Handle webhooks for successfull payment intents 
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping.data[0].shipping_details
        total = round(intent.charges.data[0].amount / 100, 2)
        
        for field, value in billing_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone_number,
                    county__iexact=shipping_details.address.county,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postcode,
                    town_or_city__iexact=shipping_details.address.town_or_city,
                    street_address1__iexact=shipping_details.address.street_address1,
                    street_address2__iexact=shipping_details.address.street_address2,
                    total=total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content = f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status = 200)
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone_number,
                        county=shipping_details.address.county,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postcode,
                        town_or_city=shipping_details.address.town_or_city,
                        street_address1=shipping_details.address.street_address1,
                        street_address2=shipping_details.address.street_address2,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle webhooks for failed payment intents
        """
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200)