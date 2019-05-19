from django.http import HttpResponse
from django.shortcuts import render_to_response
import simplejson
import json

from django.views.decorators.csrf import csrf_exempt


def register(request):
    return render_to_response('register.html')

def registerCheck(request):
    pass

def sign(request):
    return render_to_response('sign.html')

# 注意注解
@csrf_exempt
def signCheck(request):
    json_receive = simplejson.loads(request.body)
    username = json_receive['username']
    password = json_receive['password']
    # 在这里查看数据库进行用户名密码检查
    print(username)
    print(password)

    # 注意返回值
    return HttpResponse(json.dumps({
        "status": 1,
        "result": 'success',
        'username' : username,
        'password' : password,
    }))

def index(request):
    return HttpResponse('welcome to style change !')

def home(request):
    return render_to_response('home.html')