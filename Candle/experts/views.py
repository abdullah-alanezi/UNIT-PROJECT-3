from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout

# Create your views here.

def experts_view(request:HttpRequest):
    
    experts_users = User.objects.filter(groups__name='Experts')
    
    return render(request,'experts/experts.html',{'experts_users':experts_users})