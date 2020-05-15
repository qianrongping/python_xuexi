import multiprocessing
import time

def task():
    #for i in range(10):

    while True:
        print('执行任务中...')
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    sub_precess = multiprocessing.Process(target=task)

    # 把子进程设置成为守护主进程，以后主进程退出子进程直接销毁
    # sub_precess.daemon =True

    # 启动
    sub_precess.start()

    # 主进程延迟0.5s、
    time.sleep(0.5)

    # 退出主进程之前，先让子进程进行销毁
    sub_precess.terminate()
    print('over')