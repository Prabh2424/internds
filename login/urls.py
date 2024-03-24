# from django.urls import path
# from . import views


# urlpatterns = [
#     path('login/', views.log_in, name='log_in'),
#     path('logout/', views.log_out, name='log_out'),
#     path('signup/', views.sign_up, name='sign_up'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='log_in'),
    path('logout/', views.log_out, name='log_out'),
    path('signup/', views.sign_up, name='sign_up'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
]