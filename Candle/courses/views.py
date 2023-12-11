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
                    course_content = CourseContent(course=course,video_title=request.POST['video_title'],description=request.POST['description'],video_file=request.FILES['video_file'])
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
    
     
    if request.method =='post':
        course.title=request.POST['title']
        if 'image' in request.FILES:
            course.image=request.FILES['image']
        
        course.save()
        return redirect('courses:expert_course')

    
    return render(request,'courses/update_course.html',{'course':course})


def course_detile_view(request:HttpRequest,course_id):
    course = Course.objects.get(id=course_id)
    course_content = CourseContent.objects.filter(course=course)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if 'subscribe' in request.POST:
                course.subcriptions.add(request.user)

    return render(request,'courses/course_detile.html',{'course_content':course_content,'course':course})


def subscribed_courses(request:HttpRequest):
    user = request.user
    subscribed_courses = user.subscriptions.all()


    if request.method == 'POST':
        # Assuming you have a form or button to handle unsubscription
        course_id_to_unsubscribe = request.POST.get('unsubscribe_course_id')
        if course_id_to_unsubscribe:
            course = course_id_to_unsubscribe
            user.subscriptions.remove(course)

    return render(request, 'courses/subscribed_courses.html', {'subscribed_courses': subscribed_courses})



def delete_cours_econtent(request:HttpRequest,content_id):

    msg=None
    if request.user.is_authenticated and request.user.has_perm('courses.delete_course'):
        try:
            course_content= CourseContent.objects.get(id=content_id)
            course_content.delete()
        except Exception as e :
            msg=e
        return redirect('courses:course_detile_view',request.user.id)
    else: return redirect('main:no_premissions')
   

