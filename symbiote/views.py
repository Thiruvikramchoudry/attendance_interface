from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import details

# Create your views here.

def main(request):
    return render(request,'symbiote/login.html')


def login(request):
    username=request.POST['username']
    password=request.POST['password']
    print(username,password)
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return render(request,'symbiote/index.html',{'username':username})
    return redirect('/')
