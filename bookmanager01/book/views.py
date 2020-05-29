from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from book.models import BookInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    # render(request,'',context)

    return HttpResponse('index')


# 新增数据
# 方式一
book = BookInfo(
    name='python',
    pub_date='2020-01-01'
)
# 需要手动调用save
book.save()

# 方式二  直接入库
# objects 模型的管理类
# 我们对模型的 增删改查 都找它

BookInfo.objects.create(
    name='java',
    pub_date='2020-05-29'
)
