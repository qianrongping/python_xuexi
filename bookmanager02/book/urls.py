from django.conf.urls import url
from book.views import index, detail,set_cookie

urlpatterns = [
    # name 给url取一个别名
    # 可以通过name 找到这个路由
    url(r'^index/$', index, name='index'),

    # http://127.0.0.1:8000/分类id/书籍id/.
    # http://127.0.0.1: 8000/category_ id/book_ id/
    # 分组来获取正则中的数据
    # \d 整数   +: 至少匹配一个
    # url(r'^(\d+)/(\d+)/$', detail),

    # 关键字参数
    url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', detail),
    url(f'^set_cookie/$', set_cookie),
]
