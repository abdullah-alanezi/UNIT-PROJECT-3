from django.urls import path
from .import views

app_name = 'experts'

urlpatterns = [
    path('experts/',views.experts_view,name='experts_view'),
    
]