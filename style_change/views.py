from django.shortcuts import render
import json
from django.http import JsonResponse
from Deep_Learning_StyleChange.neural_style import start
import base64
import sqlite3
import os
from django.http import HttpResponse
# Create your views here.
common_path="E:/Pycharm/workspace/style_change_web/"
DB_path="E:/Pycharm/workspace/style_change_web/user.db"


temp_path="E:/Pycharm/workspace/style_change_web/temp_test/"

def index(request):
    return render(request, 'change.html')

def start_change(request):
    print("Change Starts")

  #加了数据库再用
    # name = request.GET.get('user')
    # image=start(name)

#临时测试使用案例
    image=start("temp_test")

    # image2=imageToStr(image)
    return HttpResponse("OK")

def imageToStr(image):
    with open(image,'rb') as f:
        image_byte=base64.b64encode(f.read())
        print(type(image_byte))
    image_str=image_byte.decode('ascii') #byte类型转换为str
    print(type(image_str))
    return image_str

def strToImage(str):
    image_str= str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    return image_byte

def mkdir(path):
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)