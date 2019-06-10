from django.http import HttpResponse
from django.shortcuts import render_to_response, render
import simplejson
import json
from django.forms import forms
from django.shortcuts import render
from django.http import JsonResponse
# from Deep_Learning_StyleChange.neural_style import start
import base64
import sqlite3
import os
from django.http import HttpResponse
# Create your views here.
# common_path="E:/Pycharm/workspace/style_change_web/"
# DB_path="E:/Pycharm/workspace/style_change_web/user.db"
# temp_path="E:/Pycharm/workspace/style_change_web/temp_test/"


from django.views.decorators.csrf import csrf_exempt


def register(request):
    return render_to_response('register.html')

@csrf_exempt
def registerCheck(request):
    json_receive = simplejson.loads(request.body)
    username = json_receive['username']
    password = json_receive['password']
    # 在这里查看数据库进行用户名密码检查
    print(username)
    print(password)

    # 注意返回值
    return JsonResponse({'res':1})


    # username=request.POST.get('username')
    # password=request.POST.get('password')
    # conn = sqlite3.connect('user.db')
    # c=conn.cursor()
    # cursor = c.execute("select * from user where username='%s'" % (username))
    # # 用户名已被注册
    # if (len(list(cursor)) != 0):
    #      return HttpResponse('')                #注册界面显示用户名已经被注册
    # else:
    #     c.execute("insert into USER(username,password) VALUES ('%s','%s')"%(usename,password))
    #     conn.commit()
    # conn.close()
    # return HttpResponse('sign.html')

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
    return JsonResponse({'res':1})

    # return HttpResponse(json.dumps({
    #     "status": 1,
    #     "result": 'success',
    #     'username' : username,
    #     'password' : password,
    # }))

#     MashiroCL Version
#     没用过simplejson,我用我熟悉的写一个版本吧 xD
#
    # username=request.POST.get('')   #label needed
    # password = request.POST.get('')  # label needed
    # db=sqlite3.connect(DB_path)
    # c=db.cursor()
    #
    #
    # cursor = c.execute("select * from user where username='%s'" % (username))
    # db.close()
    #
    # # 用户未注册
    # if (len(list(cursor)) == 0):
    #      return HttpResponse()      #缺一个登录需要注册界面
    #
    #@csrf_exempt
def uploadFile(request):
    if request.method == "POST":
        reverse_file =request.FILES.get("image", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not reverse_file:
            return HttpResponse("no files for upload!")

        with open(os.path.join('resource', reverse_file.name),'wb+') as f:
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

#   #加了数据库再用
#     # name = request.GET.get('user')
#     # image=start(name)
#
#     #临时测试使用案例
#     image=start("temp_test")
#
#     # image2=imageToStr(image)
#     return HttpResponse("OK")
#
# def imageToStr(image):
#     with open(image,'rb') as f:
#         image_byte=base64.b64encode(f.read())
#         print(type(image_byte))
#     image_str=image_byte.decode('ascii') #byte类型转换为str
#     print(type(image_str))
#     return image_str
#
# def strToImage(str):
#     image_str= str.encode('ascii')
#     image_byte = base64.b64decode(image_str)
#     return image_byte
#
# def mkdir(path):
#     isExists=os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)



@csrf_exempt
def uploadFile(request):
    if request.method == "POST":
        reverse_file =request.FILES.get("image", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not reverse_file:
            return HttpResponse("no files for upload!")

        with open(os.path.join('resource', reverse_file.name),'wb+') as f:
            for chunk in reverse_file.chunks():      # 分块写入文件
                f.write(chunk)

        return HttpResponse("upload over!")


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