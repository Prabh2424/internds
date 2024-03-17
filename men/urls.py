from django.urls import path
from . import views


urlpatterns = [
    path('mens/', views.men_section, name='men_section'),
]