def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0
    while current_index < num:
        result = a
        a, b = b, a + b
        current_index += 1
        yield result


# 创建生成器

f = fibonacci(10)
for value in f:
    print(value)
