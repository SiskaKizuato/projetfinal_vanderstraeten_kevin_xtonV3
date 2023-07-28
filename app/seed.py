import os
import random
from django_seed import Seed
from django.contrib.auth.hashers import make_password
from .models import Profile, ContactInfo, Category, CategoryBlog, Tag,  Blog, Partners, Article 
from django.contrib.auth import get_user_model
from django.core.files import File
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
from django.core.files.images import ImageFile
from shutil import copyfile
from django.conf import settings
BASE_DIR = settings.BASE_DIR
MEDIA_ROOT = settings.MEDIA_ROOT


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
run()


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

    seeder.add_entity(Category, 1, {'name': "Men's"})
    seeder.add_entity(Category, 1, {'name': "Women's"})
    seeder.add_entity(Category, 1, {'name': 'T-shirts'})
    seeder.add_entity(Category, 1, {'name': 'Shirts'})
    seeder.add_entity(Category, 1, {'name': 'Pants'})
    seeder.add_entity(Category, 1, {'name': 'Dresses'})
    seeder.add_entity(Category, 1, {'name': 'Jackets'})
    seeder.add_entity(Category, 1, {'name': 'Sweaters'})
    seeder.add_entity(Category, 1, {'name': 'Skirts'})
    seeder.add_entity(Category, 1, {'name': 'Shorts'})
    seeder.add_entity(Category, 1, {'name': 'Hoodies'})
    seeder.add_entity(Category, 1, {'name': 'Accessories'})

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
    blog_data = [
        {
            "title": "La beaute selon l'histoire europeenne et ta grand-mere !",
            "content": "bla bkablablabladlbwob  bwofbo o'fe  newfn eoie f",
            "date_added": "2023-07-17",
            "image": "blog_images/glamour.webp",
            "author_id": 1,
            "categoryBlog_id": 1,
            "tags_ids": [1, 2, 3],
            "views": 5
        },
        {
            "title": "Voyage sur Tatooine en Crocs Banlenciaga",
            "content": "Anakin se promenait dans les rues arides de Tatooine, portant fièrement ses Crocs Balenciaga, un mélange inattendu de style galactique et de confort terrestre. Les habitants locaux le regardaient avec étonnement, mais il se sentait à l'aise dans cette fusion unique. Ses pas légers sur le sable chaud témoignaient de son parcours de Jedi autrefois craint et respecté, maintenant imprégné d'un brin d'ironie mode. Un choix audacieux pour un homme qui a connu des ténèbres profondes, mais qui maintenant embrassait la légèreté. Tatooine était un rappel de son passé, mais ses Crocs Balenciaga lui offraient un avenir inattendu, où le style et l'aventure se rejoignaient dans une galaxie lointaine, très lointaine.",
            "date_added": "2023-07-18",
            "image": "blog_images/crocs2.jpg",
            "author_id": 1,
            "categoryBlog_id": 1,
            "tags_ids": [2, 4, 5],
            "views": 14
        },
        
	{
		"id" : 3,
		"title" : "Guccimane  ne porte t'il vraiment que du Gucci ??",
		"content" : "Vous vous etes surement deja demande si Guccimane ne porte vraiment que du Gucci ? He bien non. Voila voilouuu...",
		"date_added" : "2023-07-18",
        "image": "blog_images/gucci3.webp",
		"author_id" : 1,
		"categoryBlog_id" : 1,
        "tags_ids": [1, 3],
		"views" : 7
	},
	{
		"id" : 4,
		"title" : "Future vient-il vraiment du futur ?? Pas si sur...",
		"content" : "En fait non, il vient du passe.",
		"date_added" : "2023-07-18",
        "image": "blog_images/future2.jpg",
		"author_id" : 1,
		"categoryBlog_id" : 4,
        "tags_ids": [3],
		"views" : 33
	},
	{
		"id" : 5,
		"title" : "Les  paparazzis meritent ils la peine de mort par chatouille ?",
		"content" : "pas si sur.",
		"date_added" : "2023-07-18",
        "image": "blog_images/test.jpg",
		"author_id" : 1,
		"categoryBlog_id" : 6,
        "tags_ids": [2],
		"views" : 19
	},
	{
		"id" : 6,
		"title" : "Karl Lagerfeld, ce créateur de mode emblématique !",
		"content" : "Karl Lagerfeld était un créateur de mode emblématique, connu pour son style distinctif et sa contribution indéniable à l'industrie de la mode. Né le 10 septembre 1933 en Allemagne, Lagerfeld a laissé une empreinte durable dans le monde de la haute couture jusqu'à sa mort en février 2019.\r\n\r\nAvec son look reconnaissable, Lagerfeld était souvent vêtu de son costume noir, de ses lunettes de soleil et de son catogan argenté. Il était réputé pour son sens aiguisé de l'esthétique et sa créativité sans limites. Pendant plus de trois décennies, il a été directeur artistique de la maison de couture française Chanel, redéfinissant et modernisant la marque emblématique.",
		"date_added" : "2023-07-18",
        "image": "blog_images/karl.webp",
		"author_id" : 1,
		"categoryBlog_id" : 2,
        "tags_ids": [1, 4],
		"views" : 2
	},
	{
		"id" : 8,
		"title" : "Louis Vignac, bouteille de Vitel, verre de Cognac et Louis Vitton !",
		"content" : "lknknoinfeno oni onfefno naln nalsdndonw nowon nf jjk nwnw n n leuleu beuh",
		"date_added" : "2023-07-18",
        "image": "blog_images/lv.webp",
		"author_id" : 1,
		"categoryBlog_id" : 4,
        "tags_ids": [3, 5],
		"views" : 0
	}
        # Ajoutez d'autres blogs ici
    ]

    for blog_data in blog_data:
        author_id = blog_data['author_id']
        category_id = blog_data['categoryBlog_id']
        tags_ids = blog_data['tags_ids']

        # Vérifier si l'auteur, la catégorie et les tags existent dans la base de données
        try:
            author = Profile.objects.get(id=author_id)
            category = CategoryBlog.objects.get(id=category_id)
            tags = Tag.objects.filter(id__in=tags_ids)
        except Profile.DoesNotExist:
            print(f"L'auteur avec l'id {author_id} n'existe pas.")
            continue
        except CategoryBlog.DoesNotExist:
            print(f"La catégorie avec l'id {category_id} n'existe pas.")
            continue
        except Tag.DoesNotExist:
            print(f"Un ou plusieurs tags avec les ids {tags_ids} n'existent pas.")
            continue

        blog = Blog(
            title=blog_data['title'],
            content=blog_data['content'],
            date_added=blog_data['date_added'],
            image=blog_data['image'],
            author=author,
            categoryBlog=category,
            views=blog_data['views'],
            validated=True,
        )

        # Copier les images dans le répertoire 'media/blog_images/'
        
        # Sauvegarder le blog dans la base de données
        blog.save()

        # Ajouter les tags associés au blog
        blog.tags.add(*tags)

    print("Seed completed.")

seed_blogs()


def seed_partners():
    partners_data = [
        {
            "name": "Balenciaga",
            "logo": "partners_logos/logoBalenciaga.jpg",
        },
        {
            "name": "Givenchy",
            "logo": "partners_logos/logoGivenchy.png",
        },
        {
            "name": "Lacoste",
            "logo": "partners_logos/logoLacoste.webp",
        },
        {
            "name": "Gucci",
            "logo": "partners_logos/logoGucci.webp",
        },
        {
            "name": "Louis Vitton",
            "logo": "partners_logos/logoLV.jpg",
        },
        {
            "name": "Ralph Lauren",
            "logo": "partners_logos/logoRalflo.jpg",
        },
          {
            "name": "Adidas",
            "logo": "partners_logos/logoAdidas.jpg",
        },
        # Ajoutez d'autres données ici si nécessaire
    ]

    for partner_info in partners_data:
        name = partner_info["name"]
        logo = partner_info["logo"]
        Partners.objects.create(name=name, logo=logo)
        
    print("Seed completed.")
seed_partners()


# seed des articles  : 

def seed_articles():
    article_data = [
        {
            "id": 1,
            "name": "3B SPORTS ICON T-SHIRT MEDIUM FIT IN BLACK FADED",
            "price": 695.00,
            "category_id": 3,
            "image1": "article_images/tshirt1A.jpg",
            "image2": "article_images/tshirt1B.jpg",
            "image3": "article_images/tshirt1C.jpg",
            "promo": 0,
            "stock_L": 10,
            "stock_M": 25,
            "stock_S": 6,
            "stock_XL": 5,
            "stock_XS": 4,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 2,
            "name": "3B SPORTS ICON T-SHIRT MEDIUM FIT IN WHITE",
            "price": 695.00,
            "category_id": 3,
            "image1": "article_images/tshirt2A.jpg",
            "image2": "article_images/tshirt2B.jpg",
            "image3": "article_images/tshirt2C.jpg",
            "promo": 10,
            "stock_L": 22,
            "stock_M": 18,
            "stock_S": 7,
            "stock_XL": 8,
            "stock_XS": 0,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 3,
            "name": "SKATER T-SHIRT OVERSIZED IN BLACK FADED",
            "price": 750.00,
            "category_id": 3,
            "image1": "article_images/tshirt3A.jpg",
            "image2": "article_images/tshirt3B.jpg",
            "image3": "article_images/tshirt3C.jpg",
            "promo": 5,
            "stock_L": 17,
            "stock_M": 7,
            "stock_S": 0,
            "stock_XL": 12,
            "stock_XS": 0,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 4,
            "name": "BALENCIAGA T-SHIRT MEDIUM FIT IN PINK",
            "price": 495.00,
            "category_id": 3,
            "image1": "article_images/tshirt4A.jpg",
            "image2": "article_images/tshirt4B.jpg",
            "image3": "article_images/tshirt4C.jpg",
            "promo": 0,
            "stock_L": 8,
            "stock_M": 22,
            "stock_S":25,
            "stock_XL": 10,
            "stock_XS": 17,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 5,
            "name": "POLITICAL CAMPAIGN T-SHIRT LARGE FIT IN OFF WHITE",
            "price": 550.00,
            "category_id": 3,
            "image1": "article_images/tshirt5A.jpg",
            "image2": "article_images/tshirt5B.jpg",
            "image3": "article_images/tshirt5C.jpg",
            "promo": 15,
            "stock_L": 6,
            "stock_M": 22,
            "stock_S":23,
            "stock_XL": 11,
            "stock_XS": 10,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 6,
            "name": "POLITICAL CAMPAIGN T-SHIRT LARGE FIT IN GREEN",
            "price": 550.00,
            "category_id": 3,
            "image1": "article_images/tshirt6A.jpg",
            "image2": "article_images/tshirt6B.jpg",
            "image3": "article_images/tshirt6C.jpg",
            "promo": 5,
            "stock_L": 6,
            "stock_M": 18,
            "stock_S": 28,
            "stock_XL": 14,
            "stock_XS": 16,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 7,
            "name": "DETACHABLE SLEEVES SHIRT LARGE FIT IN GREY",
            "price": 1900.00,
            "category_id": 4,
            "image1": "article_images/tshirt7A.jpg",
            "image2": "article_images/tshirt7B.jpg",
            "image3": "article_images/tshirt7C.jpg",
            "promo": 0,
            "stock_L": 3,
            "stock_M": 3,
            "stock_S": 3,
            "stock_XL": 2,
            "stock_XS": 2,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 8,
            "name": "DIY SHIRT OVERSIZED IN LIGHT BLUE",
            "price": 1200.00,
            "category_id": 4,
            "image1": "article_images/tshirt8A.jpg",
            "image2": "article_images/tshirt8B.jpg",
            "image3": "article_images/tshirt8C.jpg",
            "promo": 0,
            "stock_L": 3,
            "stock_M": 3,
            "stock_S": 3,
            "stock_XL": 2,
            "stock_XS": 2,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 9,
            "name": "WOMEN'S SWING SHIRT LARGE FIT IN BLACK",
            "price": 950.00,
            "category_id": 4,
            "image1": "article_images/tshirt9A.jpg",
            "image2": "article_images/tshirt9B.jpg",
            "image3": "article_images/tshirt9C.jpg",
            "promo": 0,
            "stock_L": 3,
            "stock_M": 3,
            "stock_S": 3,
            "stock_XL": 2,
            "stock_XS": 2,
            "main_category_id": 2,
            "partner": 1,
        },
        {
            "id": 10,
            "name": "MEN'S BB MONOGRAM SHORT SLEEVE SHIRT LARGE FIT IN BEIGE",
            "price": 895.00,
            "category_id": 4,
            "image1": "article_images/tshirt10A.jpg",
            "image2": "article_images/tshirt10B.jpg",
            "image3": "article_images/tshirt10C.jpg",
            "promo": 10,
            "stock_L": 5,
            "stock_M": 6,
            "stock_S": 3,
            "stock_XL": 6,
            "stock_XS": 2,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 11,
            "name": "MEN'S BB MONOGRAM MINIMAL SHORT SLEEVE SHIRT IN BLACK",
            "price": 1100.00,
            "category_id": 4,
            "image1": "article_images/tshirt11A.jpg",
            "image2": "article_images/tshirt11B.jpg",
            "image3": "article_images/tshirt11C.jpg",
            "promo": 10,
            "stock_L": 5,
            "stock_M": 8,
            "stock_S": 5,
            "stock_XL": 6,
            "stock_XS": 1,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 12,
            "name": "MEN'S GRAFFITI SHIRT OVERSIZED IN BLACK",
            "price": 1400.00,
            "category_id": 4,
            "image1": "article_images/tshirt12A.jpg",
            "image2": "article_images/tshirt12B.jpg",
            "image3": "article_images/tshirt12C.jpg",
            "promo": 5,
            "stock_L": 9,
            "stock_M": 6,
            "stock_S": 5,
            "stock_XL": 6,
            "stock_XS": 1,
            "main_category_id": 1,
            "partner": 1,
        },
        {
            "id": 13,
            "name": "3-STRIPES HOODIE",
            "price": 75.00,
            "category_id": 11,
            "image1": "article_images/hoodie1A.avif",
            "image2": "article_images/hoodie1B.avif",
            "image3": "article_images/hoodie1C.avif",
            "promo": 30,
            "stock_L": 19,
            "stock_M": 26,
            "stock_S": 35,
            "stock_XL": 6,
            "stock_XS": 11,
            "main_category_id": 1,
            "partner": 7,
        },
        {
            "id": 14,
            "name": "ADICOLOR CLASSICS TREFOIL HOODIE",
            "price": 65.00,
            "category_id": 11,
            "image1": "article_images/hoodie2A.avif",
            "image2": "article_images/hoodie2B.avif",
            "image3": "article_images/hoodie2C.avif",
            "promo": 20,
            "stock_L": 17,
            "stock_M": 26,
            "stock_S": 25,
            "stock_XL": 6,
            "stock_XS": 16,
            "main_category_id": 1,
            "partner": 7,
        },
        {
            "id": 15,
            "name": "ADICOLOR OVERSIZE HOODIE",
            "price": 90.00,
            "category_id": 11,
            "image1": "article_images/hoodie3A.avif",
            "image2": "article_images/hoodie3B.avif",
            "image3": "article_images/hoodie3C.avif",
            "promo": 30,
            "stock_L": 7,
            "stock_M": 6,
            "stock_S": 15,
            "stock_XL": 5,
            "stock_XS": 12,
            "main_category_id": 2,
            "partner": 7,
        },
        {
            "id": 16,
            "name": "ESSENTIALS LINEAR FULL-ZIP FRENCH TERRY HOODIE (PLUS SIZE)",
            "price": 60.00,
            "category_id": 11,
            "image1": "article_images/hoodie4A.avif",
            "image2": "article_images/hoodie4B.avif",
            "image3": "article_images/hoodie4C.avif",
            "promo": 0,
            "stock_L": 17,
            "stock_M": 4,
            "stock_S": 5,
            "stock_XL": 10,
            "stock_XS": 2,
            "main_category_id": 2,
            "partner": 7,
        },
        {
            "id": 17,
            "name": "MANCHESTER UNITED 23/24 AWAY SHORTS",
            "price": 45.00,
            "category_id": 10,
            "image1": "article_images/short1A.avif",
            "image2": "article_images/short1B.avif",
            "image3": "article_images/short1C.avif",
            "promo": 0,
            "stock_L": 13,
            "stock_M": 24,
            "stock_S": 25,
            "stock_XL": 14,
            "stock_XS": 22,
            "main_category_id": 1,
            "partner": 7,
        },
        {
            "id": 18,
            "name": "REAL MADRID 23/24 AWAY SHORTS",
            "price": 45.00,
            "category_id": 10,
            "image1": "article_images/short2A.avif",
            "image2": "article_images/short2B.avif",
            "image3": "article_images/short2C.avif",
            "promo": 0,
            "stock_L": 16,
            "stock_M": 18,
            "stock_S": 2,
            "stock_XL": 4,
            "stock_XS": 32,
            "main_category_id": 1,
            "partner": 7,
        },
        {
            "id": 19,
            "name": "ADICOLOR 70S HIGH-WAIST MONOGRAM SHORTS",
            "price": 55.00,
            "category_id": 10,
            "image1": "article_images/short3A.avif",
            "image2": "article_images/short3B.avif",
            "image3": "article_images/short3C.avif",
            "promo": 0,
            "stock_L": 16,
            "stock_M": 18,
            "stock_S": 2,
            "stock_XL": 4,
            "stock_XS": 32,
            "main_category_id": 2,
            "partner": 7,
        },
        {
            "id": 20,
            "name": "ISLAND CLUB SHORTS",
            "price": 40.00,
            "category_id": 10,
            "image1": "article_images/short4A.avif",
            "image2": "article_images/short4B.avif",
            "image3": "article_images/short4C.avif",
            "promo": 0,
            "stock_L": 16,
            "stock_M": 19,
            "stock_S": 22,
            "stock_XL": 7,
            "stock_XS": 32,
            "main_category_id": 2,
            "partner": 7,
        },
    ]


    for data in article_data:
        category_id = data['category_id']
        main_category_id = data['main_category_id']
        partner_id = data['partner']

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            print(f"La catégorie avec l'id {category_id} n'existe pas.")
            continue

        try:
            main_category = Category.objects.get(id=main_category_id)
        except Category.DoesNotExist:
            print(f"La catégorie avec l'id {main_category_id} n'existe pas.")
            continue
        
        try:
            partner = Partners.objects.get(id=partner_id)
        except Partners.DoesNotExist:
            print(f"Le partenaire avec l'id {partner_id} n'existe pas.")
            continue

        article = Article(
            name=data['name'],
            category=category,
            main_category=main_category,
            price=data['price'],
            image1=data['image1'],
            image2=data['image2'],
            image3=data['image3'],
            stock_XS=data['stock_XS'],
            stock_S=data['stock_S'],
            stock_L=data['stock_L'],
            stock_M=data['stock_M'],
            stock_XL=data['stock_XL'],
            promo=data['promo'],
            partner=partner,
        )
        article.save()

    print("Articles seeded.")

seed_articles()