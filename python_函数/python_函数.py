"""
定义函数findall，要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，

需要找出里面所有的"hello"的位置，返回的格式是一个元组，即：(0,10,21,29)

li = 'helloworldhellopythonhelloc++hellojava'


def find_all(li):
    ret_li = []
    start_index = 0
    while True:
        ret = li.find('hello', start_index)
        if ret != -1:
            ret_li.append(ret)
            start_index = ret + 5
        else:
            break
    return ret_li


print(find_all(li))

"""

"""
定义一个函数 sum_test 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并打印结果。



def sum_test(n):
    i = 0
    sum = 0

    while i < n + 1:
        sum += i

        i += 1

    return sum


print(sum_test(4))
"""

"""
 定义一个函数，接受三个参数，分别为字符串s1、字符串s1、字符串s1，判断字符串的长度,如果三个字符串中有一个长度超过6,就进行错误提示
如果没有超过,就返回三和字符串拼接之后的结果



def add_str(s1, s2, s3):
    # if len(s1) > 6 or len(s2) > 6 or len(s3) > 6:
    # return '字符串长度超过6'
    if len(s1) > 6:
        return f'字符串{s1}长度超过6'
    elif len(s2) > 6:
        return f'字符串{s2}长度超过6'
    elif len(s3) > 6:
        return f'字符串{s3}长度超过6'
    else:
        return s1 + s2 + s3


result = add_str('asfaf', '', 'ahaf112jhn')
print(result)


"""

"""
 使用不定长参数定义一个函数max_min，接受的参数类型是数值，最终返回这些数中的最大值和最小值
 """


def max_min(*args):
    print(args)
    print(type(args))
    return max(args), min(args)


result = max_min(1, 2, 3, 4, 5)
print(result)
