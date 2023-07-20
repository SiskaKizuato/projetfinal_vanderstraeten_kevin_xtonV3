# from django.shortcuts import redirect
# from django.utils.deprecation import MiddlewareMixin


# class Block(MiddlewareMixin):
#     def init(self, get_response):
#         self.get_response = get_response

#     def process_view(self, request, view_func, view_args, view_kwargs):
#         user = request.user

#         # Admin can access all URLs, so return None to allow access
#         if user.is_authenticated and user.role == 'admin':
#             return None

#         # For stock role
#         if user.is_authenticated and user.role == 'stock':
#             if request.path in ['/allUsersBack/', '/ordersBack/', '/new_product/']:
#                 return redirect('index')

#         # For web role
#         if user.is_authenticated and user.role == 'web':
#             restricted_urls = ['/productLeftSideBar2Back/', '/allUsersBack/', '/ordersBack/', '/new_product/']
#             if request.path in restricted_urls:
#                 return redirect('home')

#         # For membre role
#         if user.is_authenticated and user.role == 'membre':
#             restricted_urls = ['/productLeftSideBar2Back/', '/allUsersBack/', '/ordersBack/', '/new_product/',
#                                '/blog5Back/', '/contactBack/', '/validationBlogBack/', '/partnersBack/', '/mailbox/']
#             if request.path in restricted_urls:
#                 return redirect('home')

#         # Redirect unauthenticated users to the login page
#         if not user.is_authenticated:
#             return redirect('login')

#         # For any other cases, return None to allow access
#         return None
