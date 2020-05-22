# 学习装饰器目的:对已有函数进行额外的功能扩展，装饰器本质上一个闭包函数，也就是说他也是一个函数嵌套
# 装饰器的特点:
# 1.不修改已有函数的源代码
# 2.不修改已有函数的调用方式
# 3.给以后函数添加额外的功能

# 定义装饰器
def decorator(func):
    def inner():
        print('已添加登录')
        func()

    return inner


@decorator
def comment():
    print('发帖')


comment()
