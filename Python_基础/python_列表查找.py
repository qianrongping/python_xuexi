name_list = ['Tom', 'Lily', 'Rose']
print(name_list)
print(name_list[0])

# index() 查找  返回定制数据所在位置的下标
# print(name_list.index('Tom'))  # 0
# print(name_list.index('Tom',0,2))
# print(name_list.index('TomS'))  # 数据不存在报错

# count(): 统计指定数据在当前列表中出现的次数。
print(name_list.count('Lily'))  # 1


# len(): 访问列表长度，即列表中数据的个数。
print(len(name_list))  # 3


# in 判断指定数据在某个列表序列，如果在返回Ture,否则返回False
print('Lily' in name_list)
# 结果:True
print('Lilys' in name_list)
# 结果: False
#体验案例
#需求:查找用户输入的名字是否已经存在。
name_list = ['Tom', 'Lily', 'Rose']
name = input('请输入您要搜索的名字: ')
if name in name_list:
    print(f'您输入的名字是{name},名字已经存在')
else:
    print(f'您输入的名字是{name},名字不存在')


# not in:判断指定数据不在某个列表序列，如果不在返回True，否则返回False

