from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


INFO = [
    {'id':1,'hostname':'lanjing-hadoop-s01','ip':'192.168.1.51','des':'hadoop','ostype':'ubuntu'},
    {'id':2,'hostname':'lanjing-hadoop-s02','ip':'192.168.1.52','des':'scrapy','ostype':'windows'},
    {'id':3,'hostname':'lanjing-hadoop-s03','ip':'192.168.1.53','des':'influx','ostype':'centos'},
]

def login(request):
    if request.method == "POST":
        print (request.POST.get('user'))
        print (request.POST.get('pwd'))
        return redirect('/home')
    else:
        print ("这是刷新页面")
    return  render(request,'login.html')

def home(request):
    return render(request,'manager.html',{'info_list':INFO})

def add(request):
    print (request.POST)
    tmp_dict = {}
    tmp_dict['id'] = request.POST.get('id')
    tmp_dict['ip'] = request.POST.get('ip')
    tmp_dict['hostname'] = request.POST.get('hostname')
    tmp_dict['ostype'] = request.POST.get('ostype')
    tmp_dict['des'] = request.POST.get('des')
    INFO.append(tmp_dict)
    print (INFO)
    return redirect('http://192.168.1.166:8090/home')

def detail(request):
    ret_id = request.GET.get('detail_id')
    ret_lst=[]
    for i in INFO:
        if int(i['id']) == int(ret_id):
            ret_lst = i
    print (ret_lst)
    return  HttpResponse(str(ret_lst))

def delete(request):
    ret_id = request.GET.get('delete_id')
    for i,j in enumerate(INFO):
        if int(j['id']) == int(ret_id):
            INFO.pop(i)

    return  HttpResponse("delete ok")
