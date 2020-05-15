"""sum = 0
i = 1
while i in range(0, 101):
    sum += i
    i += 1
    print(sum)
print(sum)"""

# sum = 0
# i = 2
# while i <= 100:
#     sum += i
#     i += 2
# print(sum)

# sum = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)

# 故事梗概:有天女朋友又生气了，惩罚:说3遍"媳妇儿，我错了"， 这个程序是不是循环即可?
# 但如果女朋友说:还要刷今天晚饭的碗，这个程序怎么书写?
# 但如果女朋友还是生气，把这套惩罚要连续3天都执行，有如何书写程序?
"""j = 0
while j < 3:
    i = 0
    while i < 3:
        print('媳妇我错了')
        i += 1
    print('刷碗')
    print('惩罚结束')
    j += 1
"""
"""
1.打印1个星星
2.行5个:循环--5个星星在行显示
3.打印5行星星:循环 一行5个

"""
"""j = 0
while j < 5:
    # 一行星星打印
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    # 一行星星结束，需要换行
    print()
    j += 1
"""

"""
j = 0
while j < 5:
    # 一行星星打印
    i = 0
    while i <= j:
        print('*', end='')
        i += 1
    # 一行星星结束，需要换行
    print()
    j += 1"""

# 九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={j*i}', end='\t')
        i += 1
    print()
    j += 1
