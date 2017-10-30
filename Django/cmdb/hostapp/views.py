from django.shortcuts import render,HttpResponse,redirect
# Create your views here.

from hostapp import models
import json

def app(request):
    return  HttpResponse('OK')


def business(request):
    if request.method == "POST":
        b_name = request.POST.get('b_name')
        models.Business.objects.create(caption=b_name)

    b_list = models.Business.objects.all()

    return render(request,'business.html',{'b_list':b_list})



def host(request):
    ret = {'status': False, 'error': None, 'data': None}
    if request.method == "POST":
        b_host = request.POST.get('b_host')
        b_port = request.POST.get('b_port')
        b_ip = request.POST.get('b_ip')
        b_bus = request.POST.get('b_bus')
        return HttpResponse(json.dumps(ret))



    h_list = models.Host.objects.all()
    b_list = models.Business.objects.all()
    return  render(request,'host.html',{'h_list':h_list,'b_list':b_list})

def test_ajax(request):
    ret = {'status':True,'error':None,'data':None}
    try:
        if request.method == "POST":
            b_host = request.POST.get('b_host')
            b_port = request.POST.get('b_port')
            b_ip = request.POST.get('b_ip')
            b_bus = request.POST.get('b_bus')
            if b_host and len(b_host) > 5:
                models.Host.objects.create(
                    hostname = b_host,
                    ip = b_ip,
                    port = b_port,
                    b_id = b_bus,
                )
            else:
                ret['status'] = False
                ret['error'] = '数据太短'

    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'

    return HttpResponse(json.dumps(ret))

def edit_host(request):
    ret = {'status':True,'error':None,'data':None}
    try:
        if request.method == "POST":
            hid = request.POST.get('hid')
            b_host = request.POST.get('b_host')
            b_port = request.POST.get('b_port')
            b_ip = request.POST.get('b_ip')
            b_bus = request.POST.get('b_bus')
            if b_host and len(b_host) > 5:
                models.Host.objects.filter(nid=hid).update(
                    hostname=b_host,
                    port=b_port,
                    ip=b_ip,
                    b_id=b_bus,
                )
            else:
                ret['status'] = False
                ret['error'] = '数据太短'
                print ('出错')
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'

    return HttpResponse(json.dumps(ret))
def del_host(request):
    ret = {'status':True,'error':None,'data':None}
    try:
        hid = request.POST.get('hid')
        models.Host.objects.filter(nid=hid).delete()
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'

    return HttpResponse(json.dumps(ret))
