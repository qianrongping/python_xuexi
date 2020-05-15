"""
1.出拳
    玩家手动输入
    电脑自动出
2.判断输赢
    2.1 玩家胜
    2.2 平局
    2.3 电脑胜
"""
import random

# 1出拳
player = int(input('请出拳：0=石头，1=剪刀，2=布： '))
computer = random.randint(0, 2)
print(computer)
# 2 判断输赢
# 玩家获胜
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 1)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
