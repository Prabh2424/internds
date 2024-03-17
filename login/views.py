from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('name')  # Assuming the field name is 'name' in your form
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, "Logged in successfully!")
            return redirect('home')  # Assuming you have a URL pattern named 'index'
        else:
            messages.error(request, "Incorrect username or password.")
    return render(request, 'sign-in.html')

def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('log_in')


def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Account created for {username}")
            return redirect('log_in')  # Adjust to your desired redirect URL
        else:
            # Form is not valid, extract error message
            error_message = form.errors.as_text()
            messages.error(request, f"Failed to create account: {error_message}")
    return render(request, 'signup.html', {'form': form})