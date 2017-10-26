from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from user import models


def login(request):
    if request.method == "GET":
        print ('刷新页面')
    if request.method == "POST":
        print (request.POST.get('user'))
        print (request.POST.get('pwd'))

    return  render(request,'login.html')


def add_user(request):
    if request.method == "POST":
        print (request.POST.get('group_id'))
        print (request.POST.get('username'))
        print (request.POST.get('password'))
        #user  = request.POST.get('user')
        #pwd   = request.POST.get('pwd')
        #外键字段-创建方式1,使用对象不推荐
        #group = models.UserGroup.objects.filter(id=1).first()
        #models.UserInfo.objects.create(username=user,password=pwd,group_id=group)

        #外键字段-创建方式2, 外键字段_id , 这儿外键字段为group_id那么插入时group_id_id
        #models.UserInfo.objects.create(username=user,password=pwd,group_id_id=2)

    group_list = models.UserGroup.objects.all()
    group_dict = {}
    for row in group_list:
        group_dict[str(row.id)] = str(row.caption)
    return  render(request,'add_user.html',{'group_dict':group_dict,'group_list':group_list})

def database(request):
    #创建用户组
    #models.UserGroup.objects.create(caption='DEV')
    #models.UserGroup.objects.create(caption='OPS')
    #models.UserGroup.objects.create(caption='TEST')
    #创建用户

    group_list = models.UserGroup.objects.all()
    for row in group_list:
        print (row.id,row.caption)

    return  HttpResponse('OK')

def home(request):
    return  render(request,'home.html')

def user_info(request):
    user_list = models.UserInfo.objects.all()
    return  render(request,'user_info.html',{'user_list':user_list})

def user_detail(request,uid):
    user = models.UserInfo.objects.filter(id=uid).first()
    return  render(request,'user_detail.html',{'user_info':user})
