from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event


# Create your views here.


def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 使用authenticate()函数认证给出的用户名和密码。它接受两个参数：username和password。并且会在用户名和密码正确的情况下返回一个user对象，否则authenticate()返回None
        user = auth.authenticate(username=username, password=password)
        # 通过if语句判断authenticate()返回对象，如果不为None，则说明用户认证通过，调用login()函数进行登录。login()函数接收HttpRequest对象和user对象
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user',username,3600)  # 添加浏览器cookie
            request.session['user'] = username  # 将session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': '用户名或密码错误!'})


# 发布会管理
@login_required()
def event_manage(request):
    # username = request.COOKIES.get('user','')   # 读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, 'event_manage.html', {"user": username,"event":event_list})
