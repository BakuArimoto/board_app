from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         try:
              user = User.objects.create_user(username, "", password)
         except IntegrityError:
              return render(request, 'signup.html', {'error':'このユーザは既に登録されています'})

    return render(request, 'signup.html')

def loginfunc(request):
    print('loginfucn start')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context':'loged in'})
        else:
            return render(request, 'login.html', {'context':'not loged in'})
    return render(request, 'login.html', {'context':'get method'})

def listfunc(request):
    return render(request, 'list.html', {})