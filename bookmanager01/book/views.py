from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from book.models import BookInfo
from book.models import PeopleInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    context = {
        'books': books
    }
    # render(request,'',context)

    return HttpResponse('index')

