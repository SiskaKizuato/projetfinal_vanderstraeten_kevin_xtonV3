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


class Article(models.Model):
    name = models.CharField(max_length=100)
    # Spécifiez un related_name différent pour le champ category
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')

    # Spécifiez un related_name différent pour le champ main_category
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_articles')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='article_images/', null=True, blank=True)    
    stock_XS = models.IntegerField()
    stock_S = models.IntegerField()
    stock_L = models.IntegerField()
    stock_M = models.IntegerField()
    stock_XL = models.IntegerField()
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

# XXXXX PARTNERS XXXXX

class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners_logos/')

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    psodo = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=500)
    lu = models.BooleanField(default=False)