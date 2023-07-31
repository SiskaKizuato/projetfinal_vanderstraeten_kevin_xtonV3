from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Block(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            if request.path in ['/allUsersBack/', '/blog5Back/', '/indexBack/', '/single-blog-1-back/', '/productsType5Back/', 'categoriesBack', '/contactBack/', '/ordersBack/', '/productLeftSideBar2Back/', '/profileBack/', '/validationBlogBack/', '/new_product/', '/partnersBack/', '/mailbox/', '/singleBlogValidation/', '/lireMail/', '/deleMail/', '/response/', '/update_contact_info/', '/update_category/', '/update_user/', '/update_profile/', '/edit_blog/', '/edit_product/', '/update_partner/', '/delete_category/', '/delete_user/', '/delete_blog/', '/delete_partner/', '/delete_article/', '/userDetailsBack/']:
                return redirect('index')

        # if request.path in ["/blogShowBackend/", "/lireBlog/<int:id>/", "/validerBlog/<int:id>/"]:
        if request.path in ["/blog5Back/", "/single-blog-1-back/", "/validationBlogBack/", "/mailbox/", "/singleBlogValidation/", "/lireMail/", "/deleMail/", "/response/", "/edit_blog/", "/delete_blog/"]:
            user = request.user
            if user.is_authenticated:
                if user.role == 'web' or user.role == 'admin':
                    return None
                else:
                    return redirect('index')
            else:
                return redirect('login')

        if request.path in ["/productsType5Back/", "/categoriesBack/", "/productLeftSideBar2Back/", "/new_product/", "/partnersBack/", "/update_category/", "/edit_product/", "/update_partner/", "/delete_category/", "/delete_partner/", "/delete_article/", "/ordersBack/"]:
            user = request.user
            if user.is_authenticated:
                if user.role == 'stock' or  user.role == 'admin':
                    return None
                else:
                    return redirect('index')
            else:
                return redirect('login')

        if request.path in ["/allUsersBack/", "/contactBack/", "/update_contact_info/", "/update_user/", "/delete_user/"]:
            user = request.user
            if user.is_authenticated:
                if user.role == 'admin':
                    return None
                else:
                    return redirect('index')
            else:
                return redirect('login')

