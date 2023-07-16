from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # XXXXX FRONT XXXXX
    path('', views.index, name="index"),
    path('indexBack', views.indexBack, name="indexBack"),
    path('blog-5/', views.blog5, name="blog5"),
    path('cart/', views.cart, name="cart"),
    path('lostPassword/', views.lostPassword, name="lostPassword"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('error-404/', views.error404, name="error404"),
    path('login_view/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout'),
    path('products-left-sidebar-2/', views.productLeftSideBar2, name="productLeftSideBar2"),
    path('products-type-1/', views.productsType1, name="productsType1"),
    path('signup/', views.signup, name="signup"),
    
    path('single-blog-1/', views.singleBlog1, name="singleBlog1"),
    path('create-blog/', views.create_blog, name='create_blog'),

    path('track-order/', views.trackOrder, name="trackOrder"),
    
    # XXXXX BACK XXXXX
    path('allUsersBack/', views.allUsersBack, name="allUsersBack"),
    path('blog5Back/', views.blog5Back, name="blog5Back"),
    path('categoriesBack/', views.categoriesBack, name="categoriesBack"),
    path('contactBack/', views.contactBack, name="contactBack"),
    path('ordersBack/', views.ordersBack, name="ordersBack"),
    path('productLeftSideBar2Back/', views.productLeftSideBar2Back, name="productLeftSideBar2Back"),
    path('profileBack/', views.profileBack, name="profileBack"),
    
    # XXXXX UPDATE XXXXX
    path('update_contact_info/', views.update_contact_info, name='update_contact_info'),
    path('update_category/<int:id>/', views.update_category, name='update_category'),
    path('update_user/<int:user_id>/', views.update_user, name='update_user'),
    path('update_profile/', views.update_profile, name='update_profile'),

    # XXXXX DELETE XXXXX
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    
    # XXXXX SHOW XXXXX
    path('userDetailsBack/<int:user_id>/', views.userDetailsBack, name='userDetailsBack'),

]
