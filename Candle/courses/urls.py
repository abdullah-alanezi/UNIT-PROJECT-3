from django.urls import path
from .import views

app_name ='courses'

urlpatterns= [

    path('add/course/',views.add_course_view,name='add_course_view'),
    path('add/course/content/<course_id>',views.add_course_content,name='add_course_content'),
    path('all/courses/',views.all_courses,name='all_courses'),
    path('my/courses/added/',views.expert_course,name='expert_course'),
    path('delete/course/<course_id>/',views.delete_course,name='delete_course'), 
    path('update/course/<course_id>/',views.update_course,name='update_course'),
    path('course/detile/<course_id>',views.course_detile_view,name='course_detile_view'),
    path('subscribed-courses/',views.subscribed_courses, name='subscribed_courses'),
    path('delete/course/content/<content_id>/',views.delete_cours_econtent,name='delete_cours_econtent')
]