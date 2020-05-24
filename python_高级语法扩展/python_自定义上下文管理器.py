class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        # 上文管理,负责返回操作对象资源,比如:文件对象,文件操作方法
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法,负责释放对象资源
        print("over")
        self.file.close()


# with 语句结合上下文管理器对象使用
with File("1.txt", "r") as file:
    # print(file.read())
    file.write("sss")
