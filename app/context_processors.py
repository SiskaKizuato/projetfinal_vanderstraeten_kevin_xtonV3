from .models import ContactInfo, Wishlist, WishlistItem

def contact_info_processor(request):
    contact_info = ContactInfo.objects.first()
    return {'contact_info': contact_info}

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
