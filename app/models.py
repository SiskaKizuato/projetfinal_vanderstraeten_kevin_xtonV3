# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from decimal import Decimal
from django.utils import timezone
from datetime import datetime


# XXXXX PARTIE USER XXXXX

class Profile(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin'
        WEB = 'web'
        STOCK = 'stock'
        MEMBRE = 'membre'
    
    role = models.CharField(choices=Role.choices, max_length=20, default=Role.MEMBRE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_user_set')

    def __str__(self):
        return self.username

# XXXXX PARTIE ARTICLE XXXXX
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners_logos/')

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100)
    # Spécifiez un related_name différent pour le champ category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    
    # Spécifiez un related_name différent pour le champ main_category
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_articles')
    partner = models.ForeignKey(Partners, on_delete=models.SET_NULL, null=True, blank=True, related_name='partners')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='article_images/', null=True, blank=True)    
    stock_XS = models.IntegerField()
    stock_S = models.IntegerField()
    stock_L = models.IntegerField()
    stock_M = models.IntegerField()
    stock_XL = models.IntegerField()
    created_at = models.DateTimeField(null=True, blank=True)
    promo = models.PositiveIntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=0)

    def __str__(self):
        return self.name

    def get_discounted_price(self):
        if self.promo > 0:
            discounted_price = self.price - (self.price * self.promo / 100)
            return Decimal(discounted_price).quantize(Decimal('0.00'))
        else:
            return self.price


# XXXXX PARTIE CONTACT XXXXX
class ContactInfo(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    fax = models.CharField(max_length=20)

    def __str__(self):
        return self.location
    
# XXXXX PARTIE BLOG XXXXX

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=70, validators=[MinLengthValidator(40)])
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    categoryBlog = models.ForeignKey('CategoryBlog', on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField(default=0)  # Champ pour stocker le nombre de vues
    validated = models.BooleanField(default=False)  # New field for validation status


    def __str__(self):
        return self.title
    
class CategoryBlog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

# XXXXX CONTACT XXXXX
    
class Contact(models.Model):
    psodo = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=500)
    lu = models.BooleanField(default=False)
    

class Wishlist(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Article)

    def __str__(self):
        return f"Wishlist for {self.user.username}"
    

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Article, on_delete=models.CASCADE)
    
class Newsletter(models.Model):
    email = models.EmailField(max_length=500,unique=True)
    # subscribe = models.BooleanField(default=False)



class Reviews(models.Model):
    commentaire = models.CharField(max_length=400)
    date_creation = models.DateTimeField(auto_now_add=True)
    produit_selected = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reviews_produit_selected')
    redacteure = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews_redacteure')
    titre = models.CharField(max_length=100)


class ReviewsVisiteur(models.Model):
    commentaire = models.CharField(max_length=400)
    date_creation = models.DateTimeField(auto_now_add=True)
    produit_selected = models.ForeignKey(Article, on_delete=models.CASCADE)
    titre = models.CharField(max_length=100)
    adresseMail = models.EmailField()
    name = models.CharField(max_length=50)
    
    
# XXXXXXX CART XXXXXXXXXXX
class Cart(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Article, through='CartItem')

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"
    
    def total_price(self):
        return self.product.price * self.quantity

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    country = models.CharField(max_length=80)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    postcode = models.CharField(max_length=6)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    promo = models.CharField(max_length=10)
    validate = models.BooleanField(default=False)
