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
    coupon = 0
    # Set the coupon code discount if it exists in the session
    if request.session.get('session_coupon'):
        coupon = request.session.get('session_coupon')
    bag = request.session.get('bag', {})
    # Get the item data and calculate the total price
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
    # Calculate new total after applying the discount
    total = total - discount
    # Put everying into the context
    context = {
        'bag_items': bag_items,
        'product_count': product_count,
        'total': total,
        'discount': discount,
        'coupon': coupon,
    }
    return context
