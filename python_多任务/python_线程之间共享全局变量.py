import threading
import time


# 全局变量
g_list = []


# 添加数据任务
def add_data():
    for i in range(3):
        g_list.append(i)
        time.sleep(0.2)
        print(i)
    print('add:', g_list)


# 读取数据任务
def read_data():
    print('read:', g_list)


if __name__ == '__main__':
    # 创建添加数据的线程
    add_thread = threading.Thread(target=add_data)
    # 创建读取任务的线程
    read_thread = threading.Thread(target=read_data)

    # 启动线程
    add_thread.start()
    # 让当前线程（主线程）等待添加数据的线程执行完以后代码再继续执行
    # add_thread.join()

    read_thread.start()
