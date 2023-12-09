from django.urls import path
from .import views

app_name ='courses'

urlpatterns= [

    path('add/course/',views.add_course_view,name='add_course_view'),
    
]