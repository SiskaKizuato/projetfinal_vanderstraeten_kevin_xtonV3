from .models import ContactInfo

def contact_info_processor(request):
    contact_info = ContactInfo.objects.first()
    return {'contact_info': contact_info}
