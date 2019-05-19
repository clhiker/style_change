from django.shortcuts import render, render_to_response
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo
# Create your views here.
def hello(request):
    return JsonResponse({'result': 200, 'msg': '连接成功'})

def index(request):
    # return HttpResponse('welcome to style change !')
    return render_to_response('sign.html')


@csrf_exempt #屏蔽装饰器器
def registerApi(request):
    if request.method == 'POST':
        req = json.loads(request.body) #取得数据
        userID = req['userID']
        pwd = req['pwd']
        searchArray = UserInfo.objects.get_or_create(username=userID) #尝试创建用户
        print(searchArray)
        if searchArray[1] == True:
            return JsonResponse({'result': 200, 'msg':'注册成功'})
        else:
            return JsonResponse({'result': 200, 'msg':'已有重复用户名'})