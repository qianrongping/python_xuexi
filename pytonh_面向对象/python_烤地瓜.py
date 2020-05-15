class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # d 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        # 1、 先计算地瓜整体烤过的时间
        self.cook_time += time
        # 2. 用整体烤过的时间 再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def cook_condiments(self,condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜考了{self.cook_time}分钟,状态是{self.cook_state},掉料是{self.condiments}'


digua1 = SweetPotato()
digua1.cook(4)
digua1.cook_condiments('辣椒面')
print(digua1)
