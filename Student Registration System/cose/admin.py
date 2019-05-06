# 管理员视图
from interface import common_interface, admin_interface
from lib import common

admin_login_info = {'name': None}


def register():
    '注册'
    while True:
        name = input('输入注册名(q\exit)>>:')
        if name == 'q': break
        if not name: continue
        pwd = input('输入密码>>:')
        new_pwd = input('再次确认密码>>:')
        if not new_pwd == pwd: continue
        flag, msg = common_interface.register_interface('admin', name, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def login():
    '登录'
    while True:
        if admin_login_info['name']:
            print('用户已登录')
            break
        name = input('输入登录名(q\exit)>>:')
        if name == 'q': break
        if not name: continue
        pwd = input('输入密码>>:')
        flag, msg = common_interface.login_interface('admin', name, pwd)
        if flag:
            print(msg)
            admin_login_info['name'] = name
            break
        else:
            print(msg)


@common.auth('admin')
def creat_school():
    '创建学校'
    while True:
        school_name = input('输入学校名字(q\exit)>>:')
        if school_name == 'q': break
        if not school_name: continue
        school_addr = input('输入地址>>:')
        if not school_addr: continue
        flsg, msg = admin_interface.creat_school(admin_login_info['name'], school_name, school_addr)
        if flsg:
            print(msg)
            break
        else:
            print(msg)


@common.auth('admin')
def creat_teacher():
    '创建老师'
    while True:
        teacher_name = input('输入老师名字(q\exit)>>:')
        if teacher_name == 'q': break
        if not teacher_name: continue
        teacher_pwd = input('输入密码>>:')
        new_pwd = input('确认密码>>:')
        if not new_pwd == teacher_pwd:
            print('密码不一致！')
            continue
        teacher_salary = input('输入薪资>>:')
        if not teacher_salary: continue
        flag, msg = admin_interface.creat_teacher(admin_login_info['name'], teacher_name, teacher_pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.auth('admin')
def creat_course():
    '创建课程'
    while True:
        school_list = common_interface.get_file('school')
        if not school_list:
            print('暂无学校信息！')
            break
        for k, v in enumerate(school_list):
            print(k, v)
        choice = input('请先选择学校编号>>:')
        if not choice.isdigit():
            print('请输入数字编号！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(school_list)):
            print('输入有误！')
            continue
        school_name = school_list[choice]
        course_name = input('请输入课程名字>>:')
        if not course_name:
            print('输入为空！')
            continue
        flag, msg = admin_interface.creat_course(admin_login_info['name'], course_name, school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': creat_school,
    '4': creat_teacher,
    '5': creat_course,
}


def admin_sys():
    '启动'
    while True:
        choice = input('''
-------------管理员系统--------------
1 注册
2 登录
3 创建学校
4 创建老师
5 创建课程
0 退出
选择操作 >>:  ''')
        if not choice.isdigit():
            print('请输入数字编号！')
            continue
        if choice == '0': break
        if not choice in func_dic: continue
        func_dic[choice]()
