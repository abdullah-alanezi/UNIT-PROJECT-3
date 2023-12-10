from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from courses.models import Course

# Create your views here.

def experts_view(request:HttpRequest):
    try:
        experts_users = User.objects.filter(groups__name='Experts')
        experts_course = Course.objects.filter()
        print(experts_course)
    except Exception:
        pass
    
    
    return render(request,'experts/experts.html',{'experts_users':experts_users})