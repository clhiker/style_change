from django.urls import path
from . import views
urlpatterns = {
    path("hello", views.hello, name='hello'), #第一个参数表示路径
    path("index", views.index, name='index'),
    path("registerApi", views.registerApi, name='registerApi')
}