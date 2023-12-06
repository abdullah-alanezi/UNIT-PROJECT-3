from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def logup_view(request:HttpRequest):

    return render(request,'users/logup.html')

def login_view(request:HttpRequest):

    return render(request,'users/login.html')

def profile_view(request:HttpRequest):

    return render(request,'users/profile.html')