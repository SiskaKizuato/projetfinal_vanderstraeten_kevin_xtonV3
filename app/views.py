from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from .forms import SignupForm, ContactInfoForm, CategoryForm, BlogForm, CategoryBlogForm, TagForm
from .models import Profile, ContactInfo, Category, Blog, CategoryBlog, Tag
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# xxxxxxxxxxxxxxxxx
# XXXXX FRONT XXXXX
# xxxxxxxxxxxxxxxxx

def index(request):
    return render(request, 'app/front/main/index.html')

def cart(request):
    return render(request, 'app/front/main/cart.html')

def checkout(request):
    return render(request, 'app/front/main/checkout.html')

def contact(request):
    # contact_info = ContactInfo.objects.first()
    # context = {'contact_info': contact_info}
    return render(request, 'app/front/main/contact.html')

def error404(request):
    return render(request, 'app/front/main/error-404.html')

def lostPassword(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User = get_user_model()
        try:
            profile = Profile.objects.get(username=username)
            if profile.email == email:
                user = profile
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                error_message = "Invalid email address."
        except Profile.DoesNotExist:
            error_message = "Invalid username."
        
        return render(request, 'app/front/main/lostPassword.html', {'error_message': error_message})
    else:
        return render(request, 'app/front/main/lostPassword.html')


def productLeftSideBar2(request):
    return render(request, 'app/front/main/products-left-sidebar-2.html')

def productsType1(request):
    return render(request, 'app/front/main/products-type-1.html')

# XXXXX COMPTE FRONT XXXXX

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'member'  # Définir le rôle de l'utilisateur en tant que membre
            user.password=make_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('index')  # Rediriger vers la page d'accueil après l'inscription
            
    else:
        form = SignupForm()
    return render(request, 'app/front/main/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'app/front/main/login.html', {'error_message': error_message})
    else:
        return render(request, 'app/front/main/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

# XXXXX BLOG FRONT XXXXX


def blog5(request):
    allBlogs = Blog.objects.all()
    categories = CategoryBlog.objects.annotate(blog_count=Count('blog'))
    tags = Tag.objects.annotate(blog_count=Count('blog'))
    return render(request, 'app/front/main/blog-5.html', {'categories': categories, 'tags': tags, 'allBlogs':allBlogs})

def singleBlog1(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'app/front/main/single-blog-1.html', {'blog': blog})


@login_required
def create_blog(request):
    tags = Tag.objects.all()
    author_username = request.user.username

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()

            selected_tags = request.POST.getlist('tags')  # Récupérer les tags sélectionnés

            # Ajouter les tags sélectionnés au blog
            for tag_id in selected_tags:
                tag = get_object_or_404(Tag, id=tag_id)
                blog.tags.add(tag)

            new_tags = request.POST.get('new_tags')

            # Créer des instances de Tag pour chaque nouveau tag et les associer au blog
            if new_tags:
                new_tags_list = [tag.strip() for tag in new_tags.split(',')]
                for tag_name in new_tags_list:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    blog.tags.add(tag)

            return redirect('blog5')
    else:
        form = BlogForm()

    tag_form = TagForm()

    return render(request, 'app/front/main/createBlog.html', {'form': form, 'tags': tags, 'tag_form': tag_form})




def trackOrder(request):
    return render(request, 'app/front/main/track-order.html')

# xxxxxxxxxxxxxxxx
# XXXXX BACK XXXXX
# xxxxxxxxxxxxxxxx

def indexBack(request):
    return render(request, 'app/back/main/indexBack.html')


# XXXXX ALL USERS XXXXX
def allUsersBack(request):
    allUsers = Profile.objects.all()

    return render(request, 'app/back/main/allUsersBack.html', {"allUsers": allUsers})

def delete_user(request, id):
    user = get_object_or_404(Profile, id=id)
    
    if request.method == 'POST':
        # Vérifier si l'utilisateur est administrateur
        if user.role == Profile.Role.ADMIN:
            # Vérifier si l'utilisateur courant est également administrateur
            if request.user == user:
                user.delete()
                messages.success(request, "Your account has been deleted successfully.")
                return redirect('index')
            else:
                messages.error(request, "Admin users cannot delete other admin users.")
        else:
            user.delete()
            messages.success(request, "User deleted successfully.")
        
        return redirect('allUsersBack')

    return redirect('allUsersBack')

def update_user(request, user_id):
    if request.method == 'POST':
        user = Profile.objects.get(id=user_id)
        role = request.POST.get('role')
        user.role = role
        user.save()
    return redirect('allUsersBack')



# XXXXX ALL BLOGS XXXXX
def blog5Back(request):
    return render(request, 'app/back/main/blog5Back.html')

# XXXXX CONTACT BACK XXXXX
def contactBack(request):
    # contact_info = ContactInfo.objects.first()
    # context = {'contact_info': contact_info}
    return render(request, 'app/back/main/contactBack.html')

def update_contact_info(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact_info)
        if form.is_valid():
            form.save()
            return redirect('contactBack')
    else:
        form = ContactInfoForm(instance=contact_info)

    return render(request, 'app/back/main/contactBack.html', {'form': form})

# XXXXX ORDERS BACK XXXXX
def ordersBack(request):
    return render(request, 'app/back/main/ordersBack.html')

def profileBack(request):
    return render(request, 'app/back/main/profileBack.html')

def productLeftSideBar2Back(request):
    return render(request, 'app/back/main/productLeftSideBar2Back.html')

# XXXXX USER DETAILS ET PROFILE XXXXX
def userDetailsBack(request, user_id):
    user = get_object_or_404(Profile, id=user_id)
    return render(request, 'app/back/main/userDetailsBack.html', {'user': user})

def profileBack(request):
    return render(request, 'app/back/main/profileBack.html')

def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.username = request.POST['username']  # Ajoutez cette ligne pour mettre à jour le nom d'utilisateur
        user.save()
        # Autres opérations de mise à jour si nécessaire
        return redirect('profileBack')
    return redirect('indexBack')


# XXXX categories XXXXX
def categoriesBack(request):
    allCategory = Category.objects.all()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categoriesBack")
    else : 
        form = CategoryForm()
    return render(request, 'app/back/main/categoriesBack.html', {"form": form, "allCategory": allCategory})

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categoriesBack')

def update_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categoriesBack')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'app/back/main/update_category.html', {'form': form, 'category': category})
