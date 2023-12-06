from django.urls import path
from . import views

app_name ='users'

urlpatterns = [
    path('logup/',views.logup_view,name='logup_view'),
    path('login/',views.login_view,name='login_view'),
    path('profile/',views.profile_view,name='profile_view')
    
]