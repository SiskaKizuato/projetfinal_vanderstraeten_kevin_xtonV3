from django import forms
from .models import Profile, Article, Category, ContactInfo, Blog, Comment, CategoryBlog, Tag

class CategoryBlogForm(forms.ModelForm):
    class Meta:
        model = CategoryBlog
        fields = '__all__'
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Fashion', 'Fashion'),
        ('Advice', 'Advice'),
        ('Tips', 'Tips'),
        ('News', 'News'),
        ('Promo', 'Promo'),
        ('Event', 'Event'),
    ]

    categoryBlog = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'categoryBlog', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']  # Ajout du champ phone
        widgets = {
            'password': forms.PasswordInput(),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['location', 'phone', 'email', 'fax']
        
