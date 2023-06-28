from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import BoardModel
from django.contrib.auth.decorators import login_required

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
            return redirect('list')
        else:
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})