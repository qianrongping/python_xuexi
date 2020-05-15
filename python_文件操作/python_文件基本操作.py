# 1.打开
f = open('test.txt', 'w')
# 2.写
#f.write('bbb')


# 读 read(nun)  num表示从文件中读取的数据的长度（字节），为空则表示去取文件中所有的数据
# print(f.read())

# readlines() 可以按照行的方式把整个问价你的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
# content = f.readlines()
# print(content)


# readline() 一次读取一行的内容
# content1 = f.readline()
# print(f'第一行：{content1}')
# content1 = f.readline()
# print(f'第二行：{content1}')


# seek() 文件指针   seek(偏移量, 起始位置)
# f.seek(5, 0)  # 文件开头
# f.seek(5, 1)  # 当前位置
# f.seek(0, 2)  # 文件结尾
# con = f.read()
# print(con)


# 3.关闭
# f.close()