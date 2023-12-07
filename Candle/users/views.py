from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
# Create your views here.

def logup_view(request:HttpRequest):
    msg= None
    try:
        if request.method == 'POST':
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
            user.save()
            return redirect('users:login_view')
    except:
        msg = "something went wrong please try later"
    return render(request,'users/logup.html',{'msg':msg})

def login_view(request:HttpRequest):

    return render(request,'users/login.html')

def profile_view(request:HttpRequest):

    return render(request,'users/profile.html')