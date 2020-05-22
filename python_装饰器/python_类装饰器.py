# 类装饰器: 使用类装饰已有函数
class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('__Call__')
        self.__func()


@MyDecorator
def show():
    print('类装饰器')


show()
