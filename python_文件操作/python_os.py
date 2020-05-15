import os

# 1.rename()  重命名   可以重命名文件、文件夹
# os.rename('test.txt', '10.txt')

# 2.remove()  删除文件
# os.remove('10.txt')

# 3.mkdir() 创建文件夹
# os.mkdir('aa')
# os.mkdir('E:/aaa')

# 4.rmdir() 删除文件夹
# os.rmdir('aa')
# os.rmdir('e:/aaa')

# 4. getcwd() 获取当前目录
# print(os.getcwd())
#
# 5. chdir()  改变默认目录
# os.mkdir('aa')
# os.chdir('aa')
# os.mkdir('bb')

# 6.listdir（） 获取目录列表  括号可以为空
# print(os.listdir())


# 批量重命名  增加、删除字符串
# 构造条件的数据
flag = 2
file_list = os.listdir()
for i in file_list:
    if flag == 1:
        new_name = 'Python' + i

    elif flag == 2:
        num = len('Python')
        new_name = i[num:]
    # 重命名
    os.rename(i, new_name)
