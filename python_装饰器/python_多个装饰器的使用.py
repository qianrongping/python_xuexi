def make_div(func):
    def inner():
        result = '<div>' + func() + '</div>'
        return result

    return inner


def make_p(func):
    def inner():
        result = '<p>' + func() + '</p>'
        return result

    return inner


# 多个装饰器的执行过程:由内到外的一个装饰过程,限制性内部的装饰器,在执行外部的装饰器
@make_div
@make_p
def content():
    return '人生苦短我用python！'


result = content()
print(result)
