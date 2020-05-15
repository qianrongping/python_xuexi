# 学员信息列表
info = []


# 1.显示功能界面
def info_pint():
    print('-' * 20)
    print('请选择功能：')
    print('1: 添加学员')
    print('2: 删除学员')
    print('3: 修改学员信息')
    print('4: 查询学员信息')
    print('5: 显示所有学员信息')
    print('6: 退出系统')
    print('-' * 20)


def add_info():
    """添加学员函数"""

    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入电话：')
    global info
    # 检测输入的姓名是否存在，存在则报错
    for i in info:
        if new_name == i['name']:
            print('学员已存在')
            return
    # 如果学员不存在，则追加
    info_dict = {}

    # 讲学员输入的数据追加到字典
    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    # 将这个学员的字典追加到列表
    info.append(info_dict)

    print(info)


def del_info():
    """删除学员"""
    # 输入要删除的学员姓名
    del_name = input('请输入要删除的学员姓名：')
    global info
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
    else:
        print('学员不存在')

    print(info)


def update_info():
    """修改学员信息"""
    # 获取需要修改的学生姓名
    update_name = input('请输入要修改的学生姓名：')
    global info
    # 判断学员是否存在，如果输入的姓名存在则修改手机号，否则提示错误
    for i in info:
        if update_name == i['name']:
            i['tel'] = input('请输入新的手机号:')
            break
    else:
        print('学员不存在')

    print(info)


def see_info():
    """查询学员信息"""
    # 输入要查找的学生姓名
    see_name = input('请输入要查找的学生姓名：')

    for i in info:
        if see_name == i['name']:
            print('查询到如下信息：')
            print(f'该学员学号是{i["id"]},姓名是{i["name"]},手机号是{i["tel"]}')
            break
    else:
        print('查无此人')


def all_info():
    """显示所有学员信息"""
    print('学号\t姓名\t手机号')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')


while True:
    # 显示功能界面
    info_pint()

    user_name = int(input("请输入功能序号："))

    # 3.按照用户输入的功能序号，执行对应功能

    if user_name == 1:
        # print('添加学员')
        add_info()
    elif user_name == 2:
        # print('删除学员')
        del_info()
    elif user_name == 3:
        # print('修改学员信息')
        update_info()
    elif user_name == 4:
        # print('查询学员信息')
        see_info()
    elif user_name == 5:
        # print('显示所有学员信息')
        all_info()
    elif user_name == 6:
        exit_glag = input('确定要退出吗？yes or no:')
        if exit_glag == 'yes':
            break
    else:
        print('输入的功能序号有误')
