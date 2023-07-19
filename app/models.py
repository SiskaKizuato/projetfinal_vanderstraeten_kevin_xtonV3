# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField()
    ranking_user = models.IntegerField(null=True, blank=True)
    ranking_global = models.DecimalField(max_digits=3, decimal_places=2)
    image1 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='article_images/', null=True, blank=True)    
    colors = models.CharField(max_length=255, blank=True)  # Champs pour les couleurs (séparées par des virgules)

    def __str__(self):
        return self.name

    def get_available_sizes(self):
        if self.category.name == "Shoes":
            return ["28", "29", "30", "31", "32"]
        elif self.category.name == "Clothing":
            return ["S", "M", "L", "XL"]
        else:
            return []

    def clean(self):
        men_count = Article.objects.filter(category__name="Men's").count()
        women_count = Article.objects.filter(category__name="Women's").count()
        clothing_count = Article.objects.filter(category__name='Clothing').count()
        shoes_count = Article.objects.filter(category__name='Shoes').count()

        if men_count > 0 and women_count > 0:
            raise ValidationError("An article cannot be both 'Men' and 'Women'.")
        
        if clothing_count > 0 and shoes_count > 0:
            raise ValidationError("An article cannot be both 'Clothing' and 'Shoes'.")

        # Vérifier si la taille est valide pour la catégorie
        if self.size_stock:
            available_sizes = self.get_available_sizes()
            for size, quantity in self.size_stock.items():
                if size not in available_sizes:
                    raise ValidationError(f"Invalid size '{size}' for this category.")

class Stock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.article.name} - Size: {self.size} - Quantity: {self.quantity}"


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
