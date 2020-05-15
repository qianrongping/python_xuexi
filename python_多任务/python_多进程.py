import multiprocessing
import time


def dance():
    for i in range(5):
        print('跳舞中')
        time.sleep(0.2)


def sing():
    for i in range(5):
        print('唱歌中。。。')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建跳舞的子进程
    # group：表示进程组，目前只能使用none
    # target：表示执行的目标任务名（函数名，方法名）
    # name： 进程名，默认是Process-1,....
    dance_process = multiprocessing.Process(target=dance, name='myprocess1')
    sing_process = multiprocessing.Process(target=sing)

    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()
