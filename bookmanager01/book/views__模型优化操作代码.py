from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from book.models import BookInfo
from book.models import PeopleInfo

############################################################## 新增数据 ##############################################################
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

############################################################### 更新数据 ##############################################################
# 方式1
# 1 先查询数据
book = BookInfo.objects.get(id=1)
# 2 更新数据:直接修改实例属性
book.read_count = 20
# 3 调用save()
book.save()

# 方式二 直接更新
BookInfo.objects.filter(id=1).update(
    read_count=100,
    comment_count=200
)

############################################################### 删除数据 ##############################################################
# 方式1
book = BookInfo.objects.get(id=4)
book.delete()
# 方式二
BookInfo.objects.filter(id=4).deletel()

############################################################### 查询数据 ##############################################################
# get 得到某一个数据
# all 获取所有的
# count 个数

# 返回一个对象
book = BookInfo.objects.get(id=1)
# 查询的id不存在会抛出异常
try:
    book = BookInfo.objects.get(id=10)
except BookInfo.DoesNotExist as e:
    pass

# 返回所有结果,是一个列表
BookInfo.objects.all()

# count
BookInfo.objects.all().count()
BookInfo.objects.count()

############################################################### filter,get,exclude ##############################################################
"""
filter,get,exclude   相当于MySQL的 where条件
filter : 筛选/过滤 返回n个结果(n=0/1/n)
get    : 返回1个结果
exclude: 排除符合条件剩下的结果  相对于not

语法形式:
    以filter(字段名__运算符=值)
    
"""
# 查询编号为1的图书
BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)
BookInfo.objects.filter(id__exact=1)

# 查询书名包含'湖'的图书
# contains 包含
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图书
# gt 大于
# gte 大于等于
# lt 小于
# lte 小于等于
BookInfo.objects.filter(gt__id=3)

# 查询书籍id不为3的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

############################################################### F对象 ##############################################################
"""
F对象的语法形式
filter(字段名__运算符=F('字段名'))

"""
from django.db.models import F

# 例：查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(read_count__gte=F('comment_count'))

# 例：查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(read_count__gte=F('comment_count') * 2)

############################################################### Q对象 ##############################################################

# 需要查询id大于2  并且阅读量大于20的书籍
# 方式1
BookInfo.objects.filter(id__gt=2).filter(read_count__gt=10)

# 方式2
BookInfo.objects.filter(id__gt=2, read_count__gt=20)

# 需要查询id大于2  或者 阅读量大于20的书
from django.db.models import Q

"""
Q(字段名__运算符=值)
或: Q()|Q() ..
并且: Q()&Q() ..
not: ~Q()
"""
BookInfo.objects.filter(Q(id__gt=2) | Q(read_count__gt=10))

############################################################### 聚合函数 ##############################################################
"""
sum,max,min.avg,count
聚合函数需要使用 aggregate
语法形式:aggregate(xxx('字段'))
"""
# 查询当前数据的阅读总量
from django.db.models import Sum, Avg, Max, Min, Count

BookInfo.objects.aggregate(Sum('read_count'))

############################################################### 排序 ##############################################################
# 默认升序
BookInfo.objects.all().order_by('read_count')
# 降序  字段+一个  - 号
BookInfo.objects.all().order_by('-read_count')

############################################################### 关联查询 ##############################################################

"""
书籍和人物的关系是  1:n
书籍 中没有任何关于任务的字段
任务 中有关于书籍的字段 book 外键
语法形式:
        通过书籍查询人物信息(已知主表数据,关联查询从表数据)
        主表模型.关联模型类名小写_set

        通过人物查询书籍信息(已知从表数据,关联查询主表数据)
        从表模型(实例对象).外键

"""
# 查询书籍为1的所有人物信息
# 通过书籍,查询任务
# 1 查询人物
book = BookInfo.objects.get(id=1)
# 2 根据书籍关联人物信息
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
# 1 查询人物
person = BookInfo.objects.get(id=1)
# 2 根据人物关联查询书籍
person.book
person.book.name

############################################################### 关联查询的筛选 ##############################################################
"""
书籍和人物的关系是  1:n
书籍 中没有任何关于任务的字段(不要考虑隐藏的哪个字段)
任务 中有关于书籍的字段 book 外键
语法形式:
        我们需要的是书籍信息,已知条件是人物信息
        我们需要的是主表数据,已知条件是从表信息
        filter(关联模型类名小写__字段__ 运算符=值)

        我们需要的是人物信息,已知条件是书籍信息
        我们需要是是从表数据,已知条件是主表信息
        filter(外键__字段__ 运算符=值)

"""
# 查询图书，要求图书人物为"郭靖"
# 我们需要的是图书,条件是人物
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__read_count__gt=30)

############################################################### 查询集 ##############################################################
# 这样每次都需要从数据库中查询
[book.id for book in BookInfo.objects.all()]

# 查询结果缓存到 books中, 相当于变量,下次不用再去查询数据库,
books = BookInfo.objects.all()
[book.id for book in books]

############################################################### 分页 ##############################################################
from django.core.paginator import Paginator

books = BookInfo.objects.all()
# object_list   结果集/列表
# per_page      每页多少天记录
p = Paginator(books, 2)
# 获取第几页的数据
books_page = p.page(1)
