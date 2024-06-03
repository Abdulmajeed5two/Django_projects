from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'users/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('login')  

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully')
            login(request, user)
            return redirect('login')
    return render(request, 'users/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')
