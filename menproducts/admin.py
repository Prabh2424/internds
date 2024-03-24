from django.contrib import admin
from .models import Product, Category, Customer, Order , Profile
from django.contrib.auth.models import User
# from .models import product
# Register your models here.

# @admin.register(product)
# class productModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category']


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Profile)

# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)
