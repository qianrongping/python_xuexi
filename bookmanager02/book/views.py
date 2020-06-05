from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import json


# Create your views here.

def index(request):
    # 登录成功之后需要跳转到首页
    # 注册成功之后需要跳转到首页
    # viewname 通过视图名字
    # 路由是动态获取的
    # path = reverse('index')
    # print(path)

    # 如果我们设置了namespace,这个时候需要通过namespace:name 来获取路由
    # path = reverse('book:index')
    # print(path)

    # 跳转页面
    # 登录成功之后需要跳转到首页
    # return redirect('/index/')
    # return redirect(path)

    # 注册成功之后需要跳转到首页
    # return redirect('/index/')
    # return redirect(path)

    return HttpResponse("index")


# http://127.0.0.1:8000/分类id/书籍id/.
# http://127.0.0.1:8000/category_id/book_id/
def detail(request, category_id, book_id):
    ###########################GET 查询字符串#################################
    """
    https://www.baidu.com/s?ie=utf-8&wd=itcast&rsv_pq=fdf543ed000f8688&rsv_t=8862Eb1lxc9858Ihke7VdJylicTyYs%2F3EuFyVPKcOBnv9wmTxLdhwlYL6%2F8&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100

    以? 作为一个分隔
    ?前边 表示 路由
    ?后边 表示 get方式传递的参数 称之为 查询字符串
    ?key=value&key=value...

    我们在登陆的时候会输入用户名和密码 理论上 用户名和密码都应该以POST方式进行传递
    只是为了让大家好理解,我们接下来 用 get方式来传递用户名和密码
    """
    # query_params = request.GET
    # print(query_params)
    # QueryDict: {'username': ['itcast'], 'password': ['123']}

    # #QueryDict
    # #<QueryDict: {'username': ['itcast', 'itheima'], 'password': ['123']}>
    #
    # # QueryDict 以普通的字典形式来获取 一键多值的是时候 只能获取最后的那一个值
    # # 我们想获取 一键一值的化 就需要使用 QueryDict 的get方法
    # # 我们想获取 一键多值的化 就需要使用 QueryDict 的getlist方法
    # username = query_params['username']
    # password = query_params['password']
    # print(username,password)

    # users = query_params.getlist('username')
    # print(users)
    # ['itcast', 'itheima']

    ###########################POST 表单数据#################################

    # data = request.POST
    # print(data)

    ###########################POST json数据#################################

    # body = request.body
    # body_str = body.decode()   # json 形式的字符串
    """{
    "username":"rubin",
    "password":"123"
    }
    """

    """
    json.dumps 将字典 转换为 json形式的字符串
    json.loads 讲json 形式的字符串 转换为 字典
    """
    # data = json.load(body_str)
    # print(data)

    ########################### 请求头 #################################

    # print(request.META)
    # print(request.method)

    ########################### HttpResponse #################################
    # HttpResponse
    # content 传递字符串   不要传递对象.字典 等数据
    # status 状态码
    # content_type 是一个MIME 类型    语法:  大类/小类    text/html    text/css   application/json

    ########################### JsonResponse #################################
    # from django.http import JsonResponse
    # data = {'name': 'rubin'}
    # return JsonResponse(data)

    ########################### 跳转页面(重定向 redirect) #################################

    # 跳转到首页
    # 通过reverse 这个名字来找到路径
    # path = reverse('book:index')
    # return redirect(path)
    # return redirect('http://www.baidu.com')

    return HttpResponse('detail')


"""
保存在客户端的数据叫做 cookie
    1. 流程
        第一次请求过程
        ①我们的浏览器第一次请求服务器的时候，不会携带任何cookie信息
        ②服务器接收到请求之后,发现请求中没有任何cookie信息
        ③服务器设置一个cookie.这个cookie设置在相应中
        ④我们的浏览器接收到这个相应之后，发现相应中有cookie信息,浏览器会将cookie信息保存起来
        第二次及其之后的过程
        ⑤当我们的浏览器第二次及其之后的请求都会携带cookie信息
        ⑥我们的服务器接收到请求之后,会发现请求中携带的cookie信息,这样的话就认识是谁的请求了

    2. 效果
    3. 从http协议角度深入掌握cookie的流程(远离)


保存在服务端的数据叫做 session 
    θ.概念
    1.流程
    第一次请求:
        ①我们第一次请求的时候可以携带一些信息(用户名/密码)    cookie中没有任何信息.
        ②当我们的服务器接收到这个请求之后,进行用户名和密码的验证,验证没有问题可以设置session信息
        ③在设置session信息的同时(session信息保存在服务器端).服务器会在响应头中设置一个session id
        ④客户端(浏览器)在接收到响应之后，会将cookie信息保存起来(保存sessionid的信息)
    第二次及其之后的请求:
        ⑤第二次及其之后的请求都会携带session id信息
        ⑥当服务器接收到这个请求之后，会获取到session id信息,然后进行验证,
        验证成功，则可以获取session信息(session信息保存在服务器端)
        
    2.效果
    
    3.从原理(http)角度
            第一次请求:
            ① 第一次请求,在请求头中没有携带任何cookie信息
            ② 我们在设置session的时候,session会做2件事. 
                #第一件：　将数据保存在数据库中
                #第二件：　设置一个cookie信息，这个cookie信息是以　sessionid为key  value为 xxxxx
                cookie肯定会以响应的形式在相应头中出现

            第二次及其之后的:

            ③ 都会携带 cookie信息,特别是 sessionid


"""


def set_cookie(request):
    # 1 先判断有没有cookie信息

    # 2 获取用户名
    username = request.GET.get('username')
    # 3 我们假设没有cookie信息,我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')

    response.set_cookie('username', username)

    # 4 返回响应
    return response


def get_cookie(request):
    # 服务器可以接收(查看)cookie信息
    cookies = request.COOKIES
    # cookies 就是一个字典
    username = cookies.get('username')

    # 得到用户信息后可以继续其它业务逻辑了
    return HttpResponse('get_cookie')


def set_session(request):
    # print(request.COOKIES)
    # 对用户和密码进行验证
    # 假设用户 和密码 正确
    user_id = 666
    # 设置session信息
    # request.session  理解为字典
    # 设置session的时候其实 session做了2件事
    # 第一件：　将数据保存在数据库中
    # 第二件：　设置一个　cookie，这个cookie 信息是以　session id为key
    request.session['user_id'] = user_id
    return HttpResponse


def get_session(request):
    # 请求都会带有session id 信息
    print(request.COOKIES)

    # 获取session信息, 然后进行验证
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')

    return HttpResponse('get_session')


"""
一个视图函数实现 登录  和 展示 的功能
"""


def login(request):
    if request.method == 'GET':
        # 展示登录页面
        return render(request, 'login.html')
    else:
        return HttpResponse('首页')


def demo(request):
    return HttpResponse('demo')


"""
类视图
1. 类视图需要需要继承自 View
2. 我们是通过在类视图中定义http方法 来实现不用的业务逻辑的
3. http方法的 第二个参数 就是请求实例对象

面向对象
    类视围是采用的面向对象的思路
        1.定义类试围
            ①继承自View ( from django. views import View)
            ②不同的请求方式有不同的业务逻辑
                类视图的方法就直接采用http的请求方式的名字作为我们的函数名.例如: get , post, put, delete
            ③类视图的方法的第二个参数必须是请求实例对象
                类视图的方法必须有返回值返回值是HttpResponse及其子类
        2.类视图的url引导

"""
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin  # 检测是否登录模块


class LoginView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('登录界面的展示')

    def post(self, request):
        return HttpResponse('登录的验证')


"""
模板
"""


class HomeView(View):

    def get(self, request):
        # 1 获取数据
        username = request.GET.get('username')

        # 2 组织数据
        context = {
            'username': username,
            'age': 14,
            'birthday': datetime.now(),
            'firends': ['tom', 'jack', 'rose'],
            'money': {
                '2019': 12000,
                '2020': 18000,
                '2021': 25000,
            }, 
            'desc': '<script>alert("hot")</script>'
        }
        # return render(request, 'detail.html')
        return render(request, 'index.html', context)
