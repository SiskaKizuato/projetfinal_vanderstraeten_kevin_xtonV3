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

    # Création de l'auteur
    author = User.objects.get(username='admin1')

    # Création des catégories
    category_ideas = CategoryBlog.objects.get(name='Ideas')
    category_social = CategoryBlog.objects.get(name='Social')
    category_boy = CategoryBlog.objects.get(name='Boy')
    category_platform = CategoryBlog.objects.get(name='Platform')
    category_shipping = CategoryBlog.objects.get(name='Shipping')

    # Création des tags
    tag_business = Tag.objects.get(name='Business')
    tag_design = Tag.objects.get(name='Design')
    tag_xton = Tag.objects.get(name='Xton')
    tag_fashion = Tag.objects.get(name='Fashion')
    tag_travel = Tag.objects.get(name='Travel')
    tag_smart = Tag.objects.get(name='Smart')
    tag_marketing = Tag.objects.get(name='Marketing')
    tag_tips = Tag.objects.get(name='Tips')

    # Liste des détails des blogs à créer
    blog_details = [
        {
            'title': "The #1 eCommerce blog to grow your business",
            'category': category_ideas,
            'tags': [tag_design, tag_xton],
            'image_path': 'path/to/image1.jpg'
        },
        {
            'title': "Latest ecommerce trend: The rise of shoppable posts",
            'category': category_ideas,
            'tags': [tag_business, tag_design],
            'image_path': 'path/to/image2.jpg'
        },
        {
            'title': "Building eCommerce wave: Social media shopping",
            'category': category_social,
            'tags': [tag_marketing, tag_xton],
            'image_path': 'path/to/image3.jpg'
        },
        {
            'title': "The best eCommerce blogs for online retailers",
            'category': category_boy,
            'tags': [tag_fashion, tag_smart],
            'image_path': 'path/to/image4.jpg'
        },
        {
            'title': "The best ecommerce platform for growing sales",
            'category': category_platform,
            'tags': [tag_business, tag_design],
            'image_path': 'path/to/image5.jpg'
        },
        {
            'title': "Shipping impacts your customer’s experience",
            'category': category_shipping,
            'tags': [tag_shipping, tag_tips],
            'image_path': 'path/to/image6.jpg'
        },
        {
            'title': "Discount shipping: faster and cheaper than ever",
            'category': category_platform,
            'tags': [tag_shipping, tag_tips],
            'image_path': 'path/to/image7.jpg'
        },
        {
            'title': "A green brand finding roots in sustainability",
            'category': category_shipping,
            'tags': [tag_business, tag_marketing],
            'image_path': 'path/to/image8.jpg'
        },
        # Ajoutez les détails pour les autres blogs ici
    ]

    for details in blog_details:
        # Création du blog
        blog = Blog.objects.create(
            title=details['title'],
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            date_added=make_aware(datetime(2021, 1, 29)),
            author=author,
            categoryBlog=details['category']
        )

        # Ajout des tags au blog
        blog.tags.set(details['tags'])

        # Chargement de l'image
        with open(details['image_path'], 'rb') as f:
            image = File(f)
            blog.image.save('image.jpg', image)

    print("Seed blogs completed.")
