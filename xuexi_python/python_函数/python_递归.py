# 需求:3以内数字累加和3+2+1=6
# 6=3+ 2以内数字累加和
# 2以内数字累加和=2+1以内数字累加和
# 1以内数字累加和= 1  出口

def sum_numbers(num):
    if num == 1:  # 出口
        return 1
    return num + sum_numbers(num-1)


result = sum_numbers(3)
print(result)

# 函数内部自己调用自己；  必须有出口
