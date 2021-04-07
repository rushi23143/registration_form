from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('index')
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exist.')
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Successfully Registered!')
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')