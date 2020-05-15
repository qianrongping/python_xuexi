"""
《代码题》
1、
1. 编写程序，从键盘获取用户名和密码，然后判断，如果正确就输出以下信息: "欢迎来到博学谷！"


acount = input('请输入账号：')
passw = input('请输入密码：')
if acount == 'admin' and passw == '123456':
    print("欢迎来到博学谷！")
else:
    print('账号密码错误')
"""

"""
《代码题》
2、
3. 考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，将结果打印到控制台。

            60以下不及格，60分以上为及格，70分至80分为合格，80分至90分为良好，90分以上为优秀。

             例如：

            请输入考试成绩：85

            你的成绩是良好

grade = int(input('请输入你的成绩：'))

if grade < 60:
    print('不及格')
elif (grade >= 60) and (grade < 70):
    print('及格')
elif (grade >= 70) and (grade < 80):
    print('合格')
elif (grade >= 80) and (grade < 90):
    print('良好')
else:
    print('优秀')
"""

"""
《代码题》
3、
4. 设计一个程序:
1-7七个数字，分别代表周一到周日，

如果输入的数字是6或7，输出“周末”，否则输出“工作日”


date = int(input("请输入星期几： "))
if date == 6 or date == 7:
    print('周末')
elif (date >= 1) and (date <= 5):
    print('工作日')
else:
    print('输入有误')
"""

"""
《代码题》
4、
4. 设计一个程序:
1-7七个数字，分别代表周一到周日，

如果输入的数字是1，输出“今天是周一”

如果输入的数字是2，输出“今天是周二”

如果输入的数字是3，输出“今天是周三”

如果输入的数字是4，输出“今天是周四”

如果输入的数字是5，输出“今天是周五”

如果输入的数字是6或7，输出“今天是周末”


date = int(input("请输入星期几： "))
if date == 1:
    print('今天是周一')
elif date == 2:
    print('今天是周二')
elif date == 3:
    print('今天是周三')
elif date == 4:
    print('今天是周四')
elif date == 5:
    print('今天是周五')
elif date ==6 or date ==7:
    print('今天是周末')
else:
    print('输入有误')
"""

"""
《代码题》
5、
5. 设计一个程序:
设计简易计算器，可以进行基本的加减乘除运算

num1 = int(input('请输入第一个数字: '))
n = input('请输入运算符号(+-*/)：')
num2 = int(input('请输入第二个数字: '))
if n == '+':
    print("%d%s%d = %d" % (num1, n, num2, num1 + num2))
if n == '-':
    print("%d%s%d = %d" % (num1, n, num2, num1 - num2))
if n == '*':
    print("%d%s%d = %d" % (num1, n, num2, num1 * num2))
if n == '/':
    print("%d%s%d = %d" % (num1, n, num2, num1 / num2))
"""
# name = input('输入名字：')
# print('你好%s'%name)

print ("Name:%10s Age:%8d Height:%8.2f"%("Aviad",25,1.83))