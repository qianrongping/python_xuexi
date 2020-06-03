"""
中间件的作用:每次请求好相应的时候都会调用    可以判断每次请求中是狗携带了cookie中某些信息
中间件的定义

"""
from django.http import HttpResponse


def simpl_middleware(get_response):

    def middleware(request):
        print('请求前')
        username = request.COOKIES.get('username')
        if username is None:
            print('username is None')
            return HttpResponse('没有登录')
        response = get_response(request)
        print('请求后')
        return response

    return middleware
