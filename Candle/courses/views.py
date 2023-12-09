from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Course
from django.contrib.auth.models import User
# Create your views here.


def add_course_view(request:HttpRequest):
    
    msg=None
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                add_course =Course(title=request.POST['title'],image=request.FILES['image'])
                add_course.save()
                add_course.user.set([request.user])

    except Exception as e:
        
        msg=e
    return render(request,'courses/add_course.html',{'msg':msg})