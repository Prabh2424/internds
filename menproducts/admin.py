from django.contrib import admin
from .models import Product, Category, Customer, Order

# from .models import product
# Register your models here.

# @admin.register(product)
# class productModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)