import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')
django.setup()


from app.seed import run, seed_contact_info

if __name__== '__main__':
    run()
