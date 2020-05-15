# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # super(School, self).__init__()
        # super(School, self).make_cake()
        super().__init__()
        super().make_cake()

# 3. 继承

class Prentice(School):
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

    # super（）调用父类方法
    def make_old_cake(self):
        super().__init__()
        super().make_cake()

xiaoqiu = Prentice()
xiaoqiu.make_old_cake()