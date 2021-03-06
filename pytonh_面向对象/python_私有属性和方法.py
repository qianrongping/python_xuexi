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
        # 定义私有属性
        self.__money = 2000000

    #  获取私有属性值
    def get_money(self):
        return self.__money

    # 修改私有属性值
    def set_money(self):
        self.__money = 500000

    # 定义私有方法
    def __siyou(self):
        print('这是私有方法')

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
print(xiaoqiu.get_money())
xiaoqiu.set_money()
print(xiaoqiu.get_money())