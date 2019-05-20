"""style_change URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from . import view

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

# 注意静态文件的添加方法
urlpatterns = [
    url(r'^$',              view.index, name='index'),
    url(r'^register/$',     view.register, name='register'),
    url(r'^sign/$',         view.sign, name='sign'),
    # 注意没有反斜杠
    url(r'^signCheck$',     view.signCheck, name='signCheck'),
    url(r'^home/$',         view.home, name='home'),
    url(r'^beginChange$',   view.biginChange, name='beginChange'),
    url(r'^upload_file/$',    view.upload_file, name='upload_file'),

    path("user_info/", include("user_info.urls")),
    # path("style_change_web", include("style_change_web.urls")),
    path('admin/', admin.site.urls),
    # path('style_change/', view.index),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
