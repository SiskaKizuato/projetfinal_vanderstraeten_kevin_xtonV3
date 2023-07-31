from .models import *
from datetime import datetime, timedelta  # Import timedelta here

from django.db.models import Sum

def cart_modal(request):
    message_empty = None
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)

            for cart_item in cart_items:
                if cart_item.product.promo == 0:
                    cart_item.total = cart_item.product.price * cart_item.quantity
                else:
                    cart_item.total = (cart_item.product.price - (cart_item.product.price * cart_item.product.promo / 100)) * cart_item.quantity
            sub_total = sum(cart_item.total for cart_item in cart_items)

            return {'cart_items': cart_items, "sub_total": sub_total}
        
        except Cart.DoesNotExist:
            message_empty = "Your cart is currently empty."
    return {'message_empty': message_empty}
    

def cart_counter(request):
    cart_count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_count = cart.products.aggregate(total_quantity=Sum('cartitem__quantity'))['total_quantity'] or 0
    return {'cart_counter': cart_count}


def contact_info_processor(request):
    contact_info = ContactInfo.objects.first()
    return {'contact_info': contact_info}

def recent_products_processor(request):
    seven_days_ago = datetime.now() - timedelta(days=7)
    recent_products = Article.objects.filter(created_at__gte=seven_days_ago).order_by('-created_at')[:4]
    return {'recent_products': recent_products}


def wishlist_content(request):
    wishlist_items = []
    no_wish = None
    wishlist_item_count = 0

    if request.user.is_authenticated:
        try:
            wishlist = Wishlist.objects.get(user=request.user)
            wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)
            wishlist_item_count = wishlist_items.count()
        except Wishlist.DoesNotExist:
            no_wish = "Your wishlist is currently empty."

    return {
        'wishlist_items': wishlist_items,
        "no_wish": no_wish,
        "wish_items_count": wishlist_item_count
    }
