from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    # Get the discount from settings
    discount = settings.DISCOUNT
    bag = request.session.get('bag', {})
    # Get the products and calculate the total
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            product_count += item_data
            total += item_data * product.price
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total': total,
                'discount': discount,
            })
    # Apply the discount outside of the for loop
    total = total - discount
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'discount': discount,
    }
    return context
