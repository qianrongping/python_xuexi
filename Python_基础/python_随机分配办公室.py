# 需求：3个办公室，8位老师，随机分配
"""
步骤：
1.准备数据
    1.1 8位老师--列表
    1.2 3个办公室--列表嵌套
2.分配老师到办公室
    随机分配
    老师名字写入办公室  --办公室列表追加老师名字数据
3.验证是否分配成功
    打印办公室详细信息：每个办公室老师和对应的老师名字
"""
import random

# 1.准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]

# 2.分配
for name in teachers:
    # 列表追加数据
    num = random.randint(0, 2)
    offices[num].append(name)

i = 1

for office in offices:
    print(f'办公室{i}人数是{len(office)}，老师分别是:')
    for name in office:
        print(name)

    i += 1