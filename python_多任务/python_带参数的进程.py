import multiprocessing


def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # # args 元组方式传参
    sub_process =multiprocessing.Process(target=show_info, args=('李四', 20))
    sub_process.start()

    # kwargs 字典方式传参
    sub_process1 =multiprocessing.Process(target=show_info, kwargs={'name': '李四', 'age': 20})

    # 启动进程

    sub_process1.start()