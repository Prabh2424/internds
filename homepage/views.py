from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('hello bhai')

# def men(request):
#     return HttpResponse('this is men section')

def women(request):
    return HttpResponse("this is women section")