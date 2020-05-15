# abs():求绝对值
# def add_num(a, b, f):
#     return f(a) + f(b)
#
#
# resule = add_num(5, 6, abs)
# print(resule)


# round() 四舍五入
# def add_num(a, b, f):
#     return f(a) + f(b)
#
#
# resule = add_num(1.5, 6.124541, round)
# print(resule)


# map()  map(func,lst),将传入的函数变量func作用到lst变量的每个元素中，并将结果组成新的列表
# list1 = [1, 2, 3, 4, 5, 6]
#
#
# def func(x):
#     return x ** 2
#
#
# result = map(func, list1)
# print(list(result))


# reduce()  reduce(func(x,y),lst),其中func必须有两个参数。每次func计算的结果和序列的下一个元素做累积计算
# import functools
#
# list1 = [1, 2, 3, 4, 5]
#
#
# def func(a, b):
#     return a + b
#
#
# result = functools.reduce(func, list1)
# print(result)


# filter(func,lst)函数用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象。如果要转换为列表，可以使用list()来转换
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def func(x):
#     return x % 2 == 0
#
#
# result = filter(func, list1)
# print(list(result))


# 使用map方法，把列 li = [1,2,3,4,5,6] 中偶数 乘以2 ,非偶数不变，并返回新列表
# li = [1, 2, 3, 4, 5, 6]
# def fun1(num):
#     if num % 2 ==0:
#         return num * 2
#     else:
#         return num
# result = map(fun1,li)
# print(list(result))


# 使用filter方法 去除 li = [1,2,None,3,None,5]  中的None 保留数字
# li = [1, 2, None, 3, None, 5]
# def fun1(x):
#     return x is not None
# result = filter(fun1,li)
# print(list(result))


# 使用reduce 方法对li = [1,2,3,4,5,6] 中的奇数部分进行累加
import functools
li = [1,2,3,4,5,6]
def fun1(x,y):
    if y % 2  == 0:
        return x
    else:
        return x + y
result = functools.reduce(fun1,li)
print(result)