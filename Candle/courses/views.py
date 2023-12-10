from django.shortcuts import render,redirect
from django.http import HttpRequest
from .models import Course,CourseContent
from django.contrib.auth.models import User
# Create your views here.


def add_course_view(request:HttpRequest):
    
    msg=None
    try:
        if request.user.is_authenticated and request.user.has_perm('courses.add_course'):

            if request.method == 'POST':
                if request.user.is_authenticated :
                    add_course =Course(user=request.user, title=request.POST['title'],image=request.FILES['image'])
                    add_course.save()
                return redirect("courses:expert_course")
        else:
            return redirect("main:no_premissions")
    except Exception as e:
        
        msg=e

    return render(request,'courses/add_course.html',{'msg':msg})


def add_course_content(request:HttpRequest,course_id):
    msg=None
    try:
        course =Course.objects.get(id=course_id)
    except Exception as e:
        msg =e
    if request.user.is_authenticated and request.user.has_perm('courses.add_coursecontent'):
        if request.method=='POST':
            if request.user.is_authenticated:
                try:
                    course_content = CourseContent(course=course,video_title=request.POST['video_title'],description=request.POST['description'],video_file=request.POST['video_file'])
                    course_content.save()
                except Exception as e:
                    msg =e
    else: return redirect("main:no_premissions")

    return render(request,'courses/add_course_content.html',{'course':course,'msg':msg})

def all_courses(request:HttpRequest):

    msg=None

    try:
        course = Course.objects.all()
    except Exception as e:
        msg =e

    return render(request,'courses/all_courses.html',{'courses':course,'msg':msg})

def expert_course(request:HttpRequest):

    
    if request.user.is_authenticated and request.user.has_perm('courses.view_course'):
        expert_course=Course.objects.filter(user=request.user)
        return render(request,"courses/expert_course.html",{"expert_courses":expert_course})
    else:
        return redirect('main:no_premissions')
    
def delete_course(request:HttpRequest,course_id):

    msg=None
    if request.user.is_authenticated and request.user.has_perm('courses.delete_course'):
        try:
            course=Course.objects.get(id=course_id)
            course.delete()
        except Exception as e :
            msg=e
        return redirect('courses:expert_course')
    else: return redirect('main:no_premissions')


def update_course(request:HttpRequest,course_id):
    course =Course.objects.get(id=course_id)
    course_content = CourseContent.objects.filter(course=course)   
    if request.method =='post':
        course =Course.objects.get(id=course_id)
        course_content = CourseContent.objects.filter(course=course)
    
    return render(request,'courses/update_course.html',{'course':course})