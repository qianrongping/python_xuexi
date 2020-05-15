class Furniture(object):
    """家具类"""
    def __init__(self, name, area):
        self.name = name
        self.area = area


class Hmoe(object):
    """家的类"""
    def __init__(self,address,area):
        # 地理位置
        self.address = address
        # 家的面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.funinture = []

    def __str__(self):
        return f'房子的地址位置在{self.address},面积是{self.area},剩余面积是{self.free_area},家具有{self.funinture}'

    def add_furniture(self,item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.funinture.append(item.name)
            # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 家具面积
            self.free_area -= item.area
        else:
            print("家具太大，剩余面积不足，无法搬入")

# 双人床 ，6
bed = Furniture('双人床', 6)
# 房子1 ：北京，200
jia1 = Hmoe('北京',200)
jia1.add_furniture(bed)
print(jia1)

sofa = Furniture('沙发', 10)
jia1.add_furniture(sofa)
print(jia1)

ball = Furniture('篮球场',200)
jia1.add_furniture(ball)
print(jia1)