import os
import random
from django_seed import Seed
from django.contrib.auth.hashers import make_password
from .models import Profile, ContactInfo, Category, CategoryBlog, Tag,  Blog, Partners
from django.contrib.auth import get_user_model
from django.core.files import File
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

# seed_tags()
# def seed_blogs():
#     User = get_user_model()
#     seeder = Seed.seeder()
#     datas = [
#         {
#             "categoryBlog": random.choice(CategoryBlog.objects.all()),
#             "date_added": datetime.now(),
#             "title": "Mon titre",
#             "content": "azeroiughgdsiujvheiujvbhzeoifihjvbzeoivhjbeohuhvbaouihihvbaoehbvaoejhjbvozjdjhbv ozeuhvbzeijhvbeouhvbzouhvbozeurhbv",
#             "image": "blog_images/3_ZhLLWyM.jpg",
#             "author": None,  # Utilisation de None pour l'instant
#             'tags': [
#                 Tag.objects.get(name='Business'),
#                 Tag.objects.get(name='Travel'),
#                 Tag.objects.get(name='Colors'),
#             ],
#         },
#     ]

#     for item in datas:
#         profile = Profile.objects.create(
#             id=1,  # Spécification de l'ID 1
#             username='admin1',
#             password=make_password('1234'),
#             email='admin1@example.com',
#             first_name='Admin',
#             last_name='Role',
#             role=Profile.Role.ADMIN,
#             phone=random.choice(phone_numbers)
#         )
#         post = Blog.objects.create(
#             categoryBlog=item['categoryBlog'],
#             date_added=item['date_added'],
#             title=item['title'],
#             content=item['content'],
#             image=item['image'],
#             author=profile,
#         )
#         post.tags.set(item['tags'])

#     print("Seed completed successfully.")

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
		"content" : "Vous vous  etes surement deja demande si Guccimane ne porte vraiment que du Gucci ? He bien non. Voila voilouuu...",
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