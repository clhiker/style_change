from django.http import HttpResponse
from django.shortcuts import render_to_response

def register(request):
    return render_to_response('register.html')

def sign(request):
    return render_to_response('sign.html')

def index(request):
    return HttpResponse('welcome to style change !')