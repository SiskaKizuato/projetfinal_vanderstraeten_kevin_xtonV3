from django import forms
from .models import Profile, Article, Category, ContactInfo, Blog, Comment, CategoryBlog, Tag

# XXXXX PARTIE BLOG XXXXX
class CategoryBlogForm(forms.ModelForm):
    class Meta:
        model = CategoryBlog
        fields = '__all__'
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogForm(forms.ModelForm):
    categoryBlog = forms.ModelChoiceField(
        queryset=CategoryBlog.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tags = forms.MultipleChoiceField(
        choices=[],
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    new_tags = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add new tags (separated by comma)'}))

    # Ajouter un champ de fichier pour la mise à jour de l'image du blog
    update_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].choices = [(tag.id, tag.name) for tag in Tag.objects.all()]

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'categoryBlog', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categoryBlog': forms.Select(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


# XXXXX PARTIE USER XXXXX
class SignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']  # Ajout du champ phone
        widgets = {
            'password': forms.PasswordInput(),
        }

# XXXXX PARTIE ARTICLE XXXXX
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

# XXXXX PARTIE CONTACT XXXXX
class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['location', 'phone', 'email', 'fax']
        
