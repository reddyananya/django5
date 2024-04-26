from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import RegistrationForm
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Received form data: username={username}, email={email}, password={password}")
            # Create a new user object
            user = User.objects.create_user(username=username, email=email, password=password)
            print("User created successfully")
            # Optionally, you can perform additional operations on the user object here
            # For example, send a confirmation email
            # Redirect to the login page after successful registration
            return redirect('login')
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Received login data: username={username}, password={password}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the home page upon successful login
                return redirect('role_selection')
            else:
                # If authentication fails, display an error message
                form.add_error(None, 'Invalid username or password')
                print("Authentication failed")
        else:
            print("Form is not valid. Errors:", form.errors)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def role_selection(request):
    return render(request, 'role_selection.html')
