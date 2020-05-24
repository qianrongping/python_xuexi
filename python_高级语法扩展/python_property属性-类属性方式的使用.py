class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def get_age(self):
        print("获取私有属性")
        return self.__age

    def set_age(self, new_age):
        print("设置私有属性")
        if 0 <= new_age <= 120:
            # new_age >= 0 and new_age <= 120:
            self.__age = new_age

        else:
            print("成精啦")

    # get_age 表示获取age属性的时候执行的代码
    # set_age 表示设置age属性的时候执行的代码
    age = property(get_age, set_age)


student = Student()
age = student.age
print(age)

student.age = 22
age = student.age
print(age)
