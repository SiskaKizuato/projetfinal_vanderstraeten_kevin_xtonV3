import random
from django_seed import Seed
from django.contrib.auth.hashers import make_password
from .models import Profile, ContactInfo, Category, CategoryBlog, Tag
from django.contrib.auth import get_user_model
from django.core.files import File
from django.utils.timezone import make_aware
from datetime import datetime
from .models import Blog, CategoryBlog, Tag

# XXXXX PARTIE USER XXXXX
def run():
    seeder = Seed.seeder()
    phone_numbers = ['+1234567890', '+9876543210', '+32435879564', '+33475802930']  # Liste de numéros de téléphone

    seeder.add_entity(Profile, 1, {
        'username': 'admin1',
        'password': make_password('1234'),
        'email': 'admin1@example.com',
        'first_name': 'Admin',
        'last_name': 'Role',
        'role': Profile.Role.ADMIN,
        'phone': random.choice(phone_numbers)  # Numéro de téléphone aléatoire
    })

    seeder.add_entity(Profile, 1, {
        'username': 'web1',
        'password': make_password('1234'),
        'email': 'web1@example.com',
        'first_name': 'Web',
        'last_name': 'Role',
        'role': Profile.Role.WEB,
        'phone': random.choice(phone_numbers)  # Numéro de téléphone aléatoire
    })

    seeder.add_entity(Profile, 1, {
        'username': 'stock1',
        'password': make_password('1234'),
        'email': 'stock1@example.com',
        'first_name': 'Stock',
        'last_name': 'Role',
        'role': Profile.Role.STOCK,
        'phone': random.choice(phone_numbers)  # Numéro de téléphone aléatoire
    })

    seeder.add_entity(Profile, 1, {
        'username': 'membre1',
        'password': make_password('1234'),
        'email': 'membre1@example.com',
        'first_name': 'Membre',
        'last_name': 'Role',
        'role': Profile.Role.MEMBRE,
        'phone': random.choice(phone_numbers)  # Numéro de téléphone aléatoire
    })

    inserted_pks = seeder.execute()
    print(inserted_pks)


# XXXXX PARTIE CONTTACT XXXXX
def seed_contact_info():
    location = "Wonder Street, USA, New York"
    phone = "+01 321 654 214"
    email = "hello@xton.com"
    fax = "+123456789"
    contact_info, _ = ContactInfo.objects.get_or_create(
        defaults={'location': location, 'phone': phone, 'email': email, 'fax': fax}
    )

    print("Contact Info seeded.")

# Appelez cette fonction dans votre méthode seed_database()
seed_contact_info()

# XXXXX PARTIE ARTICLE XXXXX

def seed_categories():
    seeder = Seed.seeder()

    # Seed for men category
    seeder.add_entity(Category, 1, {'name': "Men's"})

    # Seed for women category
    seeder.add_entity(Category, 1, {'name': "Women's"})

    # Seed for clothing category
    seeder.add_entity(Category, 1, {'name': 'Clothing'})

    # Seed for shoes category
    seeder.add_entity(Category, 1, {'name': 'Shoes'})

    seeder.execute()
    print("Categories seeded.")

# Call this function to seed the categories
seed_categories()


# XXXXX PARTIE BLOG XXXXX
def seed_category_blogs():
    category_names = ['Fashion', 'Advice', 'Tips', 'News', 'Promo', 'Event', 'Ideas', 'Social', 'Platform', 'Shipping', 'Design', 'Lifestyle', 'Device']

    for category_name in category_names:
        category, _ = CategoryBlog.objects.get_or_create(name=category_name)
        print(f"CategoryBlog created: {category}")

    print("CategoryBlogs seeded.")

# Appelez cette fonction dans votre méthode seed_database()
seed_category_blogs()

def seed_tags():
        tags = ['Business', 'Travel', 'Smart', 'Marketing', 'Colors']

        for tag_name in tags:
            Tag.objects.get_or_create(name=tag_name)

        print("Seed completed.")

seed_tags()
def seed_blogs():
    User = get_user_model()
    seeder = Seed.seeder()
    datas = [
        {
            "categoryBlog": random.choice(CategoryBlog.objects.all()),
            "date_added": datetime.now(),
            "title": "Mon titre",
            "content": "azeroiughgdsiujvheiujvbhzeoifihjvbzeoivhjbeohuhvbaouihihvbaoehbvaoejhjbvozjdjhbv ozeuhvbzeijhvbeouhvbzouhvbozeurhbv",
            "image": "blog_images/3_ZhLLWyM.jpg",
            "author": None,  # Utilisation de None pour l'instant
            'tags': [
                Tag.objects.get(name='Business'),
                Tag.objects.get(name='Travel'),
                Tag.objects.get(name='Colors'),
            ],
        },
    ]

    for item in datas:
        profile = Profile.objects.create(
            id=1,  # Spécification de l'ID 1
            username='admin1',
            password=make_password('1234'),
            email='admin1@example.com',
            first_name='Admin',
            last_name='Role',
            role=Profile.Role.ADMIN,
            phone=random.choice(phone_numbers)
        )
        post = Blog.objects.create(
            categoryBlog=item['categoryBlog'],
            date_added=item['date_added'],
            title=item['title'],
            content=item['content'],
            image=item['image'],
            author=profile,
        )
        post.tags.set(item['tags'])

    print("Seed completed successfully.")