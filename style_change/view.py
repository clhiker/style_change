from django.http import HttpResponse
from django.shortcuts import render_to_response, render
import simplejson
import json
from django.forms import forms
from django.shortcuts import render
from django.http import JsonResponse
from Deep_Learning_StyleChange.neural_style import start
import DataBase
import base64
import sqlite3
import os
from django.http import HttpResponse
# Create your views here.
# common_path="E:/Pycharm/workspace/style_change_web/"
# DB_path="E:/Pycharm/workspace/style_change_web/user.db"
# temp_path="E:/Pycharm/workspace/style_change_web/temp_test/"


from django.views.decorators.csrf import csrf_exempt


global_username = 'saber'

def register(request):
    return render_to_response('register.html')


def registerCheck(request):
    json_receive = simplejson.loads(request.body)
    username = json_receive['username']
    password = json_receive['password']

    # # #检查用户名是否已经被注册
    # check=DataBase.check_user(username)
    # #未被注册
    # if(len(check)==0):
    #     DataBase.insert_user(username,password)
    #     return JsonResponse({'res': 1})
    # #已被注册
    # else:
    #     return JsonResponse({'res': 0})

    return JsonResponse({'res': 1})

def sign(request):
    return render_to_response('sign.html')

# 注意注解
@csrf_exempt
def signCheck(request):
    json_receive = simplejson.loads(request.body)
    username = json_receive['username']
    password = json_receive['password']

    global_username = username
    if not os.path.exists('resource' + os.sep + global_username):
        os.mkdir(global_username)
    print(username)

    check=DataBase.check_user(username)
    print(check[1])
    print(password)
    if(len(username)==0):
        return JsonResponse({'res': 0})

    elif(check[1]!=password):
        return JsonResponse({'res': 0})

    #成功登录
    return JsonResponse({'res': 1})

@csrf_exempt
def uploadFile(request):
    if request.method == "POST":
        reverse_file =request.FILES.get("image", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not reverse_file:
            return HttpResponse("no files for upload!")

        file_path = 'resource' + '/' + global_username + '/' + '12-content.png'
        print(file_path)
        with open(os.path.join(file_path),'wb+') as f:
            for chunk in reverse_file.chunks():      # 分块写入文件
                f.write(chunk)

        return HttpResponse("upload over!")
    # #用户名与密码不匹配
    # for row in cursor:
    #     _username=row[0]
    #     _password=row[1]
    # if (_password != password):
    #     return HttpResponse()     #缺一个密码输入错误界面
    #
    # #成功登录
    # return HttpResponse("home.html")



def index(request):
    return HttpResponse('welcome to style change !')

def home(request):
    return render_to_response('home.html')


@csrf_exempt
def beginChange(request):
    print("Change Starts")
    username = request.POST.get('begin_change')

  #加了数据库再用
    name = 'resource' + '/' + global_username
    image=start(name)
#
#     #临时测试使用案例
#     image=start("temp_test")
#
    image2=imageToStr(image)
    DataBase.update_result(username,image2)
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
#
# def mkdir(path):
#     isExists=os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)



@csrf_exempt
def uploadFile(request):
    if request.method == "POST":
        reverse_file1 =request.FILES.get("content", None)    # 获取上传的文件，如果没有文件，则默认为None
        reverse_file2 =request.FILES.get("style", None)    # 获取上传的文件，如果没有文件，则默认为None
        # if not reverse_file:
        #     return HttpResponse("no files for upload!")
        if reverse_file1:
            with open('resource'+'/'+ global_username+'/'+'12-content.png','wb+') as f:
                for chunk in reverse_file1.chunks():      # 分块写入文件
                    f.write(chunk)
        if reverse_file2:
            with open('resource'+'/'+ global_username+'/'+'12-style.jpg','wb+') as f:
                for chunk in reverse_file2.chunks():      # 分块写入文件
                    f.write(chunk)


        return HttpResponse("upload over!")

def askForFinish(request):

    if not finish_change:
        return HttpResponse(" none")
    else:
        return HttpResponse(global_username + "result-path")

# def uploadFile(request):
#     """
#     文件接收 view
#     :param request: 请求
#     :return:
#     """
#     if request.method == 'POST':
#         my_form = FileUploadForm(request.POST, request.FILES)
#         if my_form.is_valid():
#             f = my_form.cleaned_data['image']
#             handle_uploaded_file(f)
#         return HttpResponse('Upload Success')
#     else:
#         my_form = FileUploadForm()
#     return render(request, 'home.html', {'form': my_form})
#
# def handle_uploaded_file(f):
#     with open(f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#
# class FileUploadForm(forms.Form):
#     my_file = forms.FileField()