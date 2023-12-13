from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from experts.models import ExpertExperience ,ExpertProfile
from django.db import IntegrityError
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
    msg =None
    if request.method =='POST':
        
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('main:home_view')
        else:
            msg='please provide correct username and password'
    return render(request,'users/login.html',{'msg':msg})

def logout_view(request:HttpRequest):

    if request.user.is_authenticated:
        logout(request) 
        return redirect('users:login_view')

def profile_view(request:HttpRequest,user_id):
    msg=None
    try:
        experts=User.objects.filter(groups__name='Experts')

        user = User.objects.get(id=user_id)
        experiences = ExpertExperience.objects.filter(user=user)
    except Exception as e:

        msg=e
    
    return render(request,'users/profile.html',{"user":user,'experts':experts,'experiences':experiences})


def update_profile_view(request:HttpRequest):
    msg = None
    experience_field=None
    if request.user.has_perm('experts.add_expertexperience'):

        experience_field = ExpertProfile.experience_fields.choices
    if request.user.is_authenticated:
        if request.method == "POST":
            try:
            
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                
                try:
                    profile = request.user.expertprofile
                except Exception as e:
                    profile = ExpertProfile(user=user, bio=request.POST["bio"],experience_field=request.POST['experience_field'])
                    profile.save()


                
                if 'avatar' in request.FILES: profile.avatar = request.FILES["avatar"]
                profile.bio = request.POST["bio"]
                profile.save()

                return redirect("users:profile_view", user_id = request.user.id)
            

    
                
            except IntegrityError as e:
                msg = f"Please select another username"
            except Exception as e:

                msg = e
    else:
        return redirect("main:no_premissions")

    return render(request,'users/update.html',{'msg':msg,'experience_field':experience_field})


def add_experience(request:HttpRequest,user_id):

    expert_user =User.objects.get(id=user_id)
    if request .user.is_authenticated and request.user.has_perm('experts.add_expertexperience'):
        if request.method =='POST':

            expert_experience=ExpertExperience(user=expert_user,experience=request.POST['experience'],experience_years=request.POST['experience_years'])
            expert_experience.save()
        return redirect('users:profile_view',user_id)


def delete_experience(request:HttpRequest,experience_id):

    
    expert_experience=ExpertExperience.objects.get(id=experience_id)
    expert_experience.delete()
    return redirect('users:profile_view',request.user.id)