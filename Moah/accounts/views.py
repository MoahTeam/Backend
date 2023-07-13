from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import auth
from django.contrib.auth import login, logout
from users.models import User
from django.shortcuts import render, redirect
import re

#from sqlalchemy.exc import IntegrityError

#유효성 검사, 비번찾기

def signup_view(request):
    #aaaa@aaaa.aaa
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        passwordCk = request.POST.get('passwordCk')
        if email == '' or password == "":
            return render(request, 'Account/join.html', {'error' : 'email'})
        else:
            if p.match(email) == False:
                return render(request, 'Account/join.html', {'error' : 'email'})
        if password == passwordCk:
            user = User.objects.create_user(
                username = username,
                email=email,
                password=password
            )
            
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'Account/join.html', {'error' : 'password'})
    else:
        return render(request, 'Account/join.html')

        
def login_view(request):
    if request.method == 'GET':
        return render(request, 'Account/login.html', {'form': AuthenticationForm()})
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == "" or email == None:
            print("이메일 비었음")
            return render(request, 'Account/login.html', {'error' : 'email', 'password': password})
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'Account/login.html', {'error': 'error'})
        # except User.ValueError:
        #     return render(request, 'Account/login.html', {'error': 'email', 'password': password})

        if password == "" or password == None:
            return render(request, 'Account/login.html', {'error' : 'password', 'email':email})
        if user.check_password(password):
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'Account/login.html', {'error' : 'password', 'email':email})
        
def find(request):
    #make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
    pass

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main')


