from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
#from django.db import models


# Create your views here.
from user import models

def login(request):
    if request.method == "POST":
        print (request.POST.get('username'))
        print (request.POST.get('password'))
        return redirect('/home')
    else:
        print ("刷新")
    return  render(request,'login.html')

def home(request):
    models.UserGroup.objects.create(capation='DBA')
    result = models.UserGroup.objects.all()
    for row in result:
        print (row.uid,row.capation)
    return HttpResponse('home')
