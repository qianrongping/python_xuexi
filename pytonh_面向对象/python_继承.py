# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3. 继承

class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创煎饼果子技术]'

    def make_cake(self):
        # 加自己的初始化的原因：如果不加这个自己的初始化，kongfu属性值是上一次调用的init内的kongfu的属性值
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


# 徒孙类
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()
xiaoqiu.make_school_cake()
xiaoqiu.make_Master_cake()
xiaoqiu.make_cake()
print(xiaoqiu.kongfu)

# daqiu = Prentice()
# daqiu.make_cake()
#
# daqiu.make_Master_cake()
# daqiu.make_school_cake()
# print(Prentice.__mro__)  # 打印子类继承了哪些父类
