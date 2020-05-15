mystr = "hello world and itcast and itheima and Python"
# 1.find()
# print(mystr.find('and'))  # 12
# print(mystr.find('and', 15, 30))  # 23
# print(mystr.find('ands'))  # -1

# 2.index
# print(mystr.index('and'))  # 12
# print(mystr.index('and'),15,30)  # 23
# print(mystr.index('ands'))  # 查找不存在报错

# 3.count
# print(mystr.count('and', 15, 30))  # 1
# print(mystr.count('and'))  # 3
print(mystr.count('ands'))  # 0

"""
●rfind(): 和find()功能相同， 但查找方向为右侧开始。
●rindex(): 和index:()功能相同，但查找方向为右侧开始。

"""