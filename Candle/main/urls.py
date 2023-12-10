from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('',views.home_view,name='home_view'),
    path('no_premissions/',views.no_premissions,name='no_premissions'),
]