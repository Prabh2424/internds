from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def women_section (request):
    return render(request,'main-women.html')