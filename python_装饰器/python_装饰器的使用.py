import time


def decorator(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        result = end - begin
        print(result)

    return inner


@decorator
def work():
    for i in range(10000):
        print(i)


work()
