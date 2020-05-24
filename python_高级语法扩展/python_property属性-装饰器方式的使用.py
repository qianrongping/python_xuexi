class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    @property
    def age(self):
        print("获取私有属性")
        return self.__age

    # 使用property装饰器,  方法名要保持一致

    @age.setter  # 对象调用age属性设置值的时候回调用下面的方法
    def age(self, new_age):
        print("设置私有属性")
        if 0 <= new_age <= 120:
            # new_age >= 0 and new_age <= 120:
            self.__age = new_age

        else:
            print("成精啦")


student = Student()
age = student.age
print(age)

student.age = 22
age = student.age
print(age)
