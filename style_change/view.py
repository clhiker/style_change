from django.http import HttpResponse
from django.shortcuts import render_to_response
import simplejson
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
# from Deep_Learning_StyleChange.neural_style import start
import DataBase
import base64
import sqlite3
import os
import shutil
# Create your views here.
# common_path="E:/Pycharm/workspace/style_change_web/"
# DB_path="E:/Pycharm/workspace/style_change_web/user.db"
# temp_path="E:/Pycharm/workspace/style_change_web/temp_test/"



from django.views.decorators.csrf import csrf_exempt


def register(request):
    return render_to_response('register.html')

def registerCheck(request):
    try:
        json_receive = simplejson.loads(request.body)
        username = json_receive['username']
        password = json_receive['password']
        # #检查用户名是否已经被注册
        check=DataBase.check_user(username)
        #未被注册
        if(len(check)==0):
            DataBase.insert_user(username,password)
            return JsonResponse({'res': 1})
        #已被注册
        else:
            return JsonResponse({'res': 0})
    except:
        pass


# 注意注解
@csrf_exempt
def sign(request):
    if request.method == 'GET':
        return render_to_response('sign.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)

        check=DataBase.check_user(username)

        if(len(check)==0):
            return redirect('/sign')
            # return HttpResponse('404')
            # return JsonResponse({'status' : 404})

        elif(check[1]!=password):
            return redirect('/sign')
            # return HttpResponse('307')
            # return JsonResponse({'status': 307})

        #成功登录
        else:
            request.session['username'] = username
            request.session['is_login'] = True
            keep_path = 'resource' + os.sep + request.session['username']
            if not os.path.exists(keep_path):
                os.mkdir(keep_path)

            # shutil.move('./resource/saber/1.jpg', './static/image/1.jpg')
            return redirect('/home')
            # return HttpResponse('200')
            # return JsonResponse({'status': 200})
    else:
        return render(request, "sign.html")


@csrf_exempt
def uploadFile(request):
    username = request.session['username']
    if request.method == "POST":
        reverse_file1 = request.FILES.get("content", None)  # 获取上传的文件，如果没有文件，则默认为None
        reverse_file2 = request.FILES.get("style", None)  # 获取上传的文件，如果没有文件，则默认为None
        # if not reverse_file:
        #     return HttpResponse("no files for upload!")
        if reverse_file1:
            with open('resource' + '/' + username + '/' + '12-content.png', 'wb+') as f:
                for chunk in reverse_file1.chunks():  # 分块写入文件
                    f.write(chunk)
        if reverse_file2:
            with open('resource' + '/' + username + '/' + '12-style.jpg', 'wb+') as f:
                for chunk in reverse_file2.chunks():  # 分块写入文件
                    f.write(chunk)

        return HttpResponse("upload over!")


def index(request):
    # return HttpResponse('welcome to style change !')
    return HttpResponse(request.session['username'])

def home(request):
    if request.session.get('is_login', None):
        username = request.session['username']
        return render(request, 'home.html', locals())
    else:
        return redirect('/sign/')

@csrf_exempt
def beginChange(request):
    print("Change Starts")
    request.POST.get('begin_change')

  #加了数据库再用
    name = 'resource' + '/' + request.session['username']
    # image=start(name)
#
#     #临时测试使用案例
#     image=start("temp_test")
#
    image2=imageToStr(image)
    DataBase.update_result(username,image2)
    return HttpResponse("OK")
# './resource/saber/1.jpg'
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

# @csrf_exempt
# def askForFinish(request):
#     # username=request.GET.get("username")
#     username=request.session['username']
#     temp=DataBase.check_user(username)
#     if not temp[2]:
#         return JsonResponse({
#             'status': 307,
#             'file_path': ''
#         })
#     else:
#         time.sleep(1)
#         new_path = './static/image' + '/' + username + '.jpg'
#         if os.path.exists(new_path):
#             os.remove(new_path)
#         shutil.move('./resource' + '/' + username + '/' + 'test-d2000.jpg',
#                     new_path)
#         return JsonResponse({
#             'status': 200,
#             'file_path': "." + new_path
#         })

@csrf_exempt
def askForFinish(request):
    # username=request.GET.get("username")
    username=request.session['username']
    result_path = './resource' + '/' + username + '/' + 'test-d2000.jpg'
    # temp=DataBase.check_user(username)
    if not os.path.exists(result_path):
        return JsonResponse({
            'status': 307,
            'file_path': ''
        })
    else:
        new_path = './static/image' + '/' + username + '.jpg'
        if os.path.exists('.' + new_path):
            os.remove(new_path)
        shutil.move(result_path, new_path)
        return JsonResponse({
            'status': 200,
            'file_path': '.' + new_path
        })

def logout(request):
    #注销
    request.session.clear()
    return HttpResponse('')
