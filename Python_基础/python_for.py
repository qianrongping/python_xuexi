"""
《代码题》
2、
2.使用 for 循环遍历字符串 "ILoveYou"，并打印每一个字符当字符串为 "e" 的时候终止循环：
"""
# i = "ILoveYou"
# for n in i:
#     if n == 'e':
#         break
#     print(n)

"""
《代码题》
4. 编写代码模拟用户登陆。要求：用户名为 python，密码 123456，如果输入正确，打印“欢迎光临”，程序结束，
如果输入错误，提示用户输入错误并重新输入（使用while循环即可）


while True:
    accounts = input('请输入账号：')
    passws = input('请输入密码：')
    if accounts =='python' and passws =='123456':
        print('欢迎光临')
        break
    else:
        print('输入错误并重新输入')

"""

"""
求100-200(包括100和200)里面所有的素数
提示：素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
"""
for i in range(100, 201):
    for j in range(2, i):
        # 如果能被 1~i中间间的数字整除说明，这个数字不满足要求
        # % 取余，如果能整除则余数为0
        if i % j == 0:
            break
    else:
        print('%d是素数' % i)
