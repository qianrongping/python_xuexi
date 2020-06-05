import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass


class ReceiveView(View):
    def get(self, request):
        # 1. 接受参数
        data = request.GET
        username = data.get('username')
        password = data.get('password')

        return JsonResponse({'info': {'username': username}})

    def post(self, request):
        data = json.load(request.body.decode())
        username = data.get('username')
        password = data.get('password')

        return JsonResponse({'info': {'username': username}})
