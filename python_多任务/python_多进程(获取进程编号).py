import multiprocessing
import time
import os

def dance():
    # 获取当前进程（子进程的编号）
    dance_id = os.getpid()
    print('dan_id:',dance_id,multiprocessing.current_process())

    # 获取当前进程的父进程编号
    dance_parent_id = os.getppid()
    print('dance_parent_id:',dance_parent_id,multiprocessing.current_process())
    for i in range(5):
        print('跳舞中')
        time.sleep(0.2)
        # 扩展：根据子进程编号杀死子进程
        os.kill(dance_id, 9)


def sing():
    sing_id = os.getpid()
    print('dan_id:', sing_id, multiprocessing.current_process())

    # 获取当前进程的父进程编号
    sing_parent_id = os.getppid()
    print('dance_parent_id:', sing_parent_id, multiprocessing.current_process())
    for i in range(5):
        print('唱歌中。。。')
        time.sleep(0.2)


# 获取当前(主)进程的编号
main_process = os.getpid()
print('main_process:',main_process)

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

