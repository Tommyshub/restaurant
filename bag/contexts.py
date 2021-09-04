from django.shortcuts import get_object_or_404
from menu.models import Product


def percentage(percent, whole):
    """ Function for calculating percentage """
    return (percent * whole) / 100


def bag_contents(request):
    # Set initial variables
    bag_items = []
    total = 0
    product_count = 0
    discount = 0
    # Get the discount from the session
    coupon = request.session.get('session_discount')
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
                'coupon': coupon,
            })
    # Calculate the discount percentage
    discount = percentage(coupon, total)
    # Set new total
    total = total - discount
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'discount': discount,
        'coupon': coupon,
    }
    return context
