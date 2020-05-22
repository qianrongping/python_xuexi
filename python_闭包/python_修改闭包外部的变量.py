def func_out():
    num1 = 10

    def func_inner():
        # 修改闭包内使用的外部函数变量
        nonlocal num1
        num1 = 20
        result = num1 + 10
        print(result)

    return func_inner


# 创建闭包对象
new_func = func_out()
new_func()
