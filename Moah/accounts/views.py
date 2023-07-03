from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth
from django.contrib.auth import login, logout
from users.models import User
from django.shortcuts import render, redirect

#유효성 검사, 비번찾기

def signup_view(request):
    if request.method == 'POST':
        username = "hey"
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordCk = request.POST.get('passwordCk')
        if email == '' or password == "":
            return render(request, 'Account/join.html')
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
        if email == "":
            pass
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'Account/login.html')
        except User.ValueError:
            return render(request, 'Account/login.html')

        if user.check_password(password):
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'Account/login.html')
        
def find(request):
    #make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
    pass

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')


