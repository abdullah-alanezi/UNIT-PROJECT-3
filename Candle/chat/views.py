from django.shortcuts import render

from django.http import HttpRequest
# Create your views here.

def chat(request:HttpRequest):
    username = ''
    if request.method=='POST':

        username = request.POST.get('username')

    return render(request,'chat/chat.html',{'username':username})
