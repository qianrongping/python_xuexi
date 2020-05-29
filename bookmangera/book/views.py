from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from book.models import BookInfo


# Create your views here.

def index(request):
    # 把所有书籍查询出来
    books = BookInfo.objects.all()
    # 组织数据
    context = {
        'books': books
    }

    return render(request, 'index.html', context)
    # return HttpResponse('index`````')
