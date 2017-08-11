#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views #从当前目录下导入了 views 模块

app_name = 'blogapp'#指定命名空间，防止冲突
urlpatterns=[url(r'^$', views.index, name='index'),
url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
#绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数
#（第一个参数是网址，第二个参数是处理函数），
#另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名
