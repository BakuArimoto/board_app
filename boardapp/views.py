from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        print(request.POST)
        print('helo')
        # username = request.POST["username"]
        # password = request.POST["password"]

        # username = request.POST.get('username')
        # password = request.POST.get('password') 
        # print(request.POST)
    return render(request, 'signup.html', {'some':100})
