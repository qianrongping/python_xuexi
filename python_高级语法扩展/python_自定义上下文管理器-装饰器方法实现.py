from contextlib import contextmanager


# j加上装饰器这个代码,那么下面函数创建的对象就是一个上下文管理器
@contextmanager
def my_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        yield file
    except Exception as e:
        print(e)

    finally:
        file.close()


with my_open("1.txt", "r") as file:
    file_data = file.read()
    print(file_data)
