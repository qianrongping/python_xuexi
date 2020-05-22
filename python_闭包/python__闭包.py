# 闭包的作用:可以保存外部函数的变量

# 1. 函数嵌套
def func_out():
    a = 10

    def func_inner(b):
        result = a + b
        # 2. 内部函数必须使用外部函数的变量或者参数
        print(result)

    return func_inner


# 获取闭包
# 这个new_func就是闭包,等于:func_inner
new_func = func_out()
# 执行闭包
new_func(1)
