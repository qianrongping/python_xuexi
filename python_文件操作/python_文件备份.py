# 1.接收用户输入的文件名
old_name = input('请输入需要备份的文件名：')

# 2.规划备份文件名
# 2.1 提取后缀，找到名字中的点  --名字和后缀分裂
index = old_name.rfind('.')

# 有效文件才备份
if index > 0:
    postfix = old_name[index:]

# 2.2 组织新名字 = 原名字 +【备份】 + 后缀
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)
# 3.备份文件写入数据
# 3.1 打开源文件 和 备份文件
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')
# 3.2 源文件读取，备份文件写入
while True:
    con = old_f.read(1024)
    if len(con) ==0:
        break
    new_f.write(con)
# 3.3 关闭文件
old_f.close()
new_f.close()
