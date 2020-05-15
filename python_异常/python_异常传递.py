import time

try:
    f = open('text1.txt')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成，退出循环
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        print('程序被意外终止')
except:
    print('该文件不存在')
finally:
    f.close()
