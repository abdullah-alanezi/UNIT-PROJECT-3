from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def experts_view(request:HttpRequest):

    return render(request,'experts/experts.html')