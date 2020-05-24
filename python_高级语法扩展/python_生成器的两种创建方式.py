# 1 生成器推到式
my_gennerator = (value * 2 for value in range(3))
for value in my_gennerator:
    print(value)


# 2 在函数里面看到有yield关键字,那么这个函数就是生成器了
def my_generator():
    for i in range(3):
        # 当程序执行到yield关键字时代码会暂停并返回结果,再次启动生成器时会在暂停位置继续往下执行
        yield i


result = my_generator()
print(result)

for value in result:
    print(value)
