from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordCk = request.POST.get('passwordCk')
        if password == passwordCk:
            user = User.objects.create_user(
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
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'form':form})
        
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


