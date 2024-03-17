from django.urls import path
from . import views

urlpatterns = [
    path('men-products/', views.men_product, name='men_product'),

    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category')
]