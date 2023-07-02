from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        username = "hey"
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordCk = request.POST.get('passwordCk')
        if password == passwordCk:
            user = User.objects.create_user(
                username = username,
                email=email,
                password=password
            )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'Account/join.html')
    else:
        return render(request, 'Account/join.html')

        
def login_view(request):
    if request.method == 'GET':
        return render(request, 'Account/login.html', {'form': AuthenticationForm()})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.get(email=email)
        if user is None:
            pass

        if user.check_password(password):
            auth.login(request, user)
            return redirect('index')
        else:
            print("dfsdf")
            return render(request, 'Account/login.html')
        
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


