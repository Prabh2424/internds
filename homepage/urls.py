from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('men/', views.men , name='men'),
    path('woman/', views.women , name = 'women'),
]