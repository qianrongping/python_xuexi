from student import *


class StudentManager(object):
    def __init__(self):
        # 存储学员数据  --列表
        self.student_list = []

    # 程序入口函数
    def run(self):
        # 1. 加载文件里的学员信息
        self.load_student()

        while True:
            # 2. 显示功能菜单
            self.show_menu()

            # 3.用户输入功能序号

            menu_mun = int(input('请输入您需要的额功能序号：'))

            # 4. 根据用户输入的功能序号执行不同的更改
            if menu_mun == 1:
                # 添加学员
                self.add_student()

            elif menu_mun == 2:
                # 删除学员
                self.del_student()

            elif menu_mun == 3:
                # 修改学员
                self.modify_student()

            elif menu_mun == 4:
                # 查询学员
                self.search_student()

            elif menu_mun == 5:
                # 显示所有学员
                self.show_student()

            elif menu_mun == 6:
                # 保存学员
                self.sava_student()

            elif menu_mun == 7:
                # 退出系统
                break

    @staticmethod
    # 显示功能菜单 -- 打印序号的功能对应关系 -- 静态
    def show_menu():
        print('请选择如下功能----------')
        print('1：添加学员')
        print('2：删除学员')
        print('3：修改学员')
        print('4：查询学员')
        print('5：显示所有学员')
        print('6：保存学员')
        print('7:退出系统')

    # 添加学员
    def add_student(self):
        name = input('请输入姓名：')
        gender = input('请输入性别：')
        tel = input('请输入的电话：')

        # 创建学员对象 -- 类 ？类在student文件里面  先导入student模块，再创建对象
        student = Student(name, gender, tel)

        # 3. 将该对象添加到学员列表
        self.student_list.append(student)

        # print(self.student_list)
        print(student)

    # 删除学员
    def del_student(self):
        # 1. 用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2. 遍历学员列表，如果用户输入的学员存在则删除学员对象，否则提示学员不存在
        for i in self.student_list:
            if del_name == i.name:
                self.student_list.remove(i)

        else:
            print('查无此人')

        print(self.student_list)

    # 修改学员
    def modify_student(self):
        # 1. 用户输入目标学员姓名
        modify_name = input('请输入要修改的学员姓名：')
        for i in self.student_list:
            if modify_name == i.name:
                i.name = input('姓名：')
                i.gender = input('性别：')
                i.tel = input('电话:')
                print(f'修改成功，姓名：{i.name},性别：{i.gender},电话：{i.tel}')
        else:
            print('查无此人')

    # 查询学员
    def search_student(self):
        search_name = input('请输入目标学员姓名：')
        for i in self.student_list:
            if search_name == i.name:
                print(f'姓名是：{i.name}，性别是：{i.gender}，电话是：{i.tel}')

        print('查无此人')

    # 显示所有学员信息
    def show_student(self):
        # 1 打印表头
        print('姓名\t性别\t手机号')

        # 2 打印数据
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 保存学员信息
    def sava_student(self):
        # 1 打开文件
        f = open('student.data', 'w')

        # 2 文件写入数据
        # 2.1 [学员对象]转换[字典]
        new_list = [i.__dict__ for i in self.student_list]

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭
        f.close()

    def load_student(self):
        # 1 打开文件：尝试r打开，如果有异常 w
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 2 读取数据：文件读取出的数据是字符串还原列表类型；[{}] 转换 [学员对象]
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            # 3 关闭文件
            f.close()



