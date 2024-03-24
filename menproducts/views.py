from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Category
from django.contrib import messages

from django.db.models import Q
# from django.views import View

# Create your views here.

def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})	    



def men_product(request):
    all_products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'men-product.html', {'products': all_products})  # Pass the fetched products to the template context


def product(request, pk):
    product = Product.objects.get(id=pk)  # Fetch the product with the given id
    return render(request, 'product_page.html', {'product': product})  # Pass the product


def category(request, foo):
    foo = foo.replace('-', ' ')  # Replace hyphens with spaces
    try:
        category_obj = Category.objects.get(name=foo)
        product = Product.objects.filter(category=category_obj)
        return render(request,'category.html',{'product':product,'Category':category_obj})
    except:
        messages.success(request,("the category Doesn't Exist....."))
        return redirect('home')