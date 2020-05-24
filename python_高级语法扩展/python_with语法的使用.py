# try:
#     file = open("1.txt", "r")
#     file.write("abc")
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# 为了简化读取文件的操作,python提供了with语句的写法
# 当with语句执行完成,自动关闭操作的文件,即使有异常也关闭

with open("1.txt", "r") as file:
    file.write("sss")
