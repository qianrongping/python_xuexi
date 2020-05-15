"""
try:
    f = open('text.txt', 'r')

except:
    f = open('text.txt', 'w')
"""

"""
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)
"""

"""
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('我是else，是没有异常时执行的代码')
"""

# finally表示的是无论是否异常都要执行的代码，例如关闭文件。
try:
    f = open('text1.txt', 'r')
except:
    f = open('text1.txt', 'w')
else:
    print('没有异常，真开心')
finally:
    f.close()
