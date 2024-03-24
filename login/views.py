from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django import forms
from menproducts.models import Profile
import json
from cart.cart import Cart

# Create your views here.
def log_in(request):
	if request.method == 'POST':
		username = request.POST.get('name')  # Assuming the field name is 'name' in your form
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			# Do some shopping cart stuff
			current_user = Profile.objects.get(user__id=request.user.id)
			# Get their saved cart from database
			saved_cart = current_user.old_cart
			# Convert database string to python dictionary
			if saved_cart:
				# Convert to dictionary using JSON
				converted_cart = json.loads(saved_cart)
				# Add the loaded cart dictionary to our session
				# Get the cart
				cart = Cart(request)
				# Loop thru the cart and add the items from the database
				for key, value in converted_cart.items():
					cart.db_add(product=key, quantity=value)
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


def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		users_form = UpdateUserForm(request.POST or None, instance=current_user)

		if users_form.is_valid():
			users_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'users_form': users_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')


def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form': form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('update_info')


def update_info(request):
    current_user = Profile.objects.get(user=request.user)
    form = UserInfoForm(request.POST or None, instance=current_user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Your info has been updated!")
            return redirect('home')
    else:
        form = UserInfoForm(instance=current_user)

    return render(request, "update_info.html", {'user_form': form})
