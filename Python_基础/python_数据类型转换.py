# 5. eval() --计算在字符串中的有效Python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000，2000，3000) '
str5 = '[1000,2000,3000]'
print(type(eval(str2)))
print(type(eval(str3)))
