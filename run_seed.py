import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')
django.setup()


from app.seed import run, seed_contact_info, seed_category_blogs, seed_tags, seed_blogs


