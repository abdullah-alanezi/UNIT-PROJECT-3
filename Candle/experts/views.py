from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.models import User
from courses.models import Course
from .models import ExpertProfile

# Create your views here.

def experts_view(request:HttpRequest):
    experts_users=""
    msg=None
    try:
        if 'search' in request.GET:
            search_value = request.GET['search']
            experts_users = ExpertProfile.objects.filter(experience_field=search_value)

        else:
            experts_users = ExpertProfile.objects.all()
        
        
    except Exception as e:
        msg =e
        
    
    
    
    return render(request,'experts/experts.html',{'experts_users':experts_users,'experience_field':ExpertProfile.experience_fields.choices,'msg':msg})


