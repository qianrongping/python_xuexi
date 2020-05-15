import threading


# 全局变量
g_num = 0

# 创建全局互斥锁
lock = threading.Lock()


# 执行一次给全局变量+1
def sum_num1():
    #上锁
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num +=1

    print('num1', g_num)
    #释放锁
    lock.release()


# 执行一次给全局变量+1
def sum_num2():
    # 上锁
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num += 1

    print('num2', g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 创建sum1，sum2线程
    sum1_thread = threading.Thread(target=sum_num1)
    sum2_thread = threading.Thread(target=sum_num2)

    #启动线程
    sum1_thread.start()
    sum2_thread.start()