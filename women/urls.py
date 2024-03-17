from django.urls import path
from . import views
urlpatterns = [
   path('women/', views.women_section, name='women_section')
]