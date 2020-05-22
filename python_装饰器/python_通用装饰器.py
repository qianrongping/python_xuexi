# 通用的装饰器: 可以装饰任意类型的函数

# ----装饰带有不定长参数和返回值的函数-------

def decorator(func):
    # 使用装饰器装饰已有函数的时候，内部函数的类型和要装饰的已有函数的类型保持一致
    def inner(*args, **kwargs):
        # 在内部函数对已有函数进行装饰
        print('正在努力执行代码')

        # *args: 把元组里面的每一个元素，按照位置参数的方式进行传参
        # **kwargs: 把字典里面的每一个键值对，按照关键字的方式进行传参
        # 这里对元组和字典进行拆包，仅限于结合不定长参数的函数使用
        num = func(*args, **kwargs)
        return num

    return inner


@decorator
def add_num(*args, **kwargs):
    result = 0
    # args: 元组类型
    # kwargs: 字典类型

    for value in args:
        result += value

    for value in kwargs.values():
        result += value

    return result


# @decorator  # show= decorator(show) show = inner
# def show():
#     return "哈哈"

result = add_num(1, 2)
print(result)
