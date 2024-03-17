from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def men_section (request):
    return render(request,'main-men.html')

def base (request):
    return render(request,'base.html')

def prod (request):
    return render(request,'product.html')