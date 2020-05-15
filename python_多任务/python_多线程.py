import threading
import time


def dance():
    # 获取当前线程
    dance_thread_id = threading.current_thread()
    print('dance：', dance_thread_id)
    for i in range(5):
        print('跳舞中')
        time.sleep(0.2)


def sing():
    # 获取当前线程
    sing_thread_id = threading.current_thread()
    print(sing_thread_id)
    for i in range(5):
        print('唱歌中。。。')
        time.sleep(0.2)


if __name__ == '__main__':
    # 获取当前线程
    main_thread_id = threading.current_thread()
    print(main_thread_id)

    # 创建子线程
    dance_thread = threading.Thread(target=dance)
    sing_thread =threading.Thread(target=sing)

    # 启动线程
    dance_thread.start()
    sing_thread.start()
