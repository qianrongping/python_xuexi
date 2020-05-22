def return_decorator(flag):
    def decorator(func):
        def inner(a, b):
            if flag == '+':
                print('正在努力计算加法')
            elif flag == '-':
                print('正在努力计算减法')
            func(a, b)

        return inner

    return decorator


@return_decorator('+')
def add_num(a, b):
    result = a + b
    print(result)


def sub_num(a, b):
    result = a - b
    print(result)


add_num(1, 2)
sub_num(5, 2)
