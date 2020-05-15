mystr = "hello world and itcast and itheima and Python"
# 字符串是不可变数据类型


# 1.replace  --修改  返回新的字符串
# print(mystr.replace('and', 'he'))
# print(mystr.replace('and', 'he', 1))  # 替换次数如果超出子串出现的次数，表示替换所有这个子串


# 2.  --分割 返回一个列表
# print(mystr.split('and'))  # 丢失分割字符
# print(mystr.split('and', 2))


# 3. join() -- 合并列表里面的字符串数据为一个大字符串
# mylist = ['aa', 'bb', 'cc']
# new_str = '...'.join(mylist)
# print(new_str)


# capitalize(): 将字符串第一个字符转换成大写。
# 结果: Hello world and itcast and itheima and python
print(mystr.capitalize())
# 注意: capitalize)函数转换后，只字符串第-个字符大写，其他的字符全都小写。


# title(): 将字符串每个单词首字母转换成大写。
print(mystr.title())
# 结果：Hello World And Itcast And Itheima And Python


# lower(): 将字符串中大写转小写。
# 结果: hello world and itcast and itheima and python
print(mystr.lower())

# upper(): 将字符串中小写转大写。
# 结果:HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
print(mystr.upper())

# Istrip(): 删除字符串左侧空白字符。
mystr = '  he11o world and itcast and itheima and Python  '
mystr.lstrip()

# rstrip(): 删除字符串右侧空白字符。
mystr = '  he11o world and itcast and itheima and Python  '
mystr.rstrip()

# strip(): 删除字符串两侧空白字符。
mystr = '  he11o world and itcast and itheima and Python  '
mystr.strip()

# startswith() 判断字符串是否以某个子串开头
print(mystr.startswith('hello'))

# endswith() 判断字符串是否以某个子串结尾
print(mystr.endswith('Python'))

# isalpha(): 如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False。
mystr1 = 'hello'
mystr2 = 'hello12345'
print(mystr1.isalpha())
# 结果:True
print(mystr2.isalpha())
# 结果: False

# isdigit(): 如果字符串只包含数字则返回True否则返回False。
