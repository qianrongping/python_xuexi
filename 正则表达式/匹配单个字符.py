import re

# . 匹配任意1个字符(除了\n)
# [ ] 匹配 [ ] 中列举的字符
# \d 匹配数字,即0-9
# \D 匹配 非数字,既不是数字
# \s 匹配空白, 即空格  tab键
# \S 匹配非空白
# \w 匹配非特殊字符,即a-z  A-Z 0-9 _ 汉字

# . 匹配任意1个字符(除了\n)
# 1. 正则表达式
# 2.要匹配的对象

match_obj = re.match("t.o", 't\no')
if match_obj:
    # 匹配结果
    result = match_obj.group()
    print(result)
else:
    print("匹配失败")

# [ ] 匹配[ ] 中列举的字符
march_obj = re.match("葫芦娃[12]", "葫芦娃1")
if march_obj:
    # 匹配结果
    result = march_obj.group()
    print(result)
else:
    print("匹配失败")


# 匹配银行卡密码其中的一位
march_obj = re.match("[0123456789]", "7")
if march_obj:
    # 匹配结果
    result = march_obj.group()
    print(result)
else:
    print("匹配失败")

match_obj = re.match("[0-9]", "7")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")


# \d = > [0-9]= >[0123456789]
match_obj = re.match("\d", "789")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")



# \D: 匹配一个非数字字符
match_obj = re.match("\D", "a")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")


# \s: 匹配一个空白字符，空格或者tab键
match_obj = re.match("葫芦娃\s[12]", "葫芦娃 1")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")


match_obj = re.match("葫芦娃\S[12]", "葫芦娃+1")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print("没空白的匹配:", result)
else:
    # 匹配失败match_obj是一个None
    print("没空白的匹配:匹配失败")


# 匹配某网站中密码的其中一位，密码是由字母、数字、下划线组成
match_obj = re.match("[a-zA-Z0-9_]", "_")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")

# \w: 匹配一个字母、数字、下划线、汉字
match_obj = re.match("\w", "哈")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")

# \W: 匹配一个非字母、非数字、非下划线、非汉字的字符
match_obj = re.match("\W", "%")
if match_obj:
    # 获取匹配结果
    result = match_obj.group()
    print(result)
else:
    # 匹配失败match_obj是一个None
    print("匹配失败")