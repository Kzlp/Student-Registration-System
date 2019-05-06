# 学生视图
student_login_info = {'name':None}
from interface import common_interface,student_interface
from lib import common

def register():
    '注册'
    while True:
        name = input('输入注册名(q\exit)>>:')
        if name == 'q': break
        if not name: continue
        pwd = input('输入密码>>:')
        new_pwd = input('再次确认密码>>:')
        if not new_pwd == pwd: continue
        flag, msg = common_interface.register_interface('student', name, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)


def login():
    '登录'
    while True:
        if student_login_info['name']:
            print('用户已登录')
            break
        name = input('输入登录名(q\exit)>>:')
        if name == 'q': break
        if not name: continue
        pwd = input('输入密码>>:')
        flag, msg = common_interface.login_interface('student', name, pwd)
        if flag:
            print(msg)
            student_login_info['name'] = name
            break
        else:
            print(msg)

@common.auth('student')
def choice_school():
    '选择学校'
    while True:
        school_list = common_interface.get_file('school')
        if not school_list:
            print('暂无学校信息！')
            break
        for k,v in enumerate(school_list):
            print(k,v)
        choice = input('请输入学校编号(q\exit)>>:')
        if choice == 'q':break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(school_list)):
            print('输入有误！')
            continue
        school_name = school_list[choice]
        flag,msg = student_interface.choice_school_interface(student_login_info['name'],school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('student')
def choice_course():
    '选择课程'
    while True:
        school_name = student_interface.check_studene_school_interface(student_login_info['name'])
        if not school_name:
            print('请先选择学校！')
            break
        course_list = student_interface.check_school_course_interface(school_name)
        if not course_list:
            print("该校区下没有课程")
            break
        for k,v in enumerate(course_list):
            print(k,v)
        choice = input('请输入课程编号(q\exit)>>:')
        if choice == 'q':break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print('输入有误！')
            continue
        course_name = course_list[choice]
        flag, msg = student_interface.choice_course_interface(student_login_info['name'],course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth('student')
def check_score():
    '查看分数'
    while True:
        course_list = student_interface.get_student_course(student_login_info['name'])
        if not course_list:
            print('学生暂未选择课程')
            break
        for k,v in enumerate(course_list):
            print(k, v)
        choice = input('请输入查询课程编号(q\exit)>>:')
        if choice == 'q':break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print('输入有误！')
            continue
        course_name = course_list[choice]
        flag = student_interface.check_student_score(student_login_info['name'], course_name)
        print(flag)
        break
func_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def student_sys():
    '启动'
    while True:
        choice = input('''
-------------学生管理系统--------------
1 注册
2 登录
3 选择学校
4 选择课程
5 查看分数
0 退出
选择操作 >>:  ''')
        if not choice.isdigit():
            print('请输入数字编号！')
            continue
        if choice == '0': break
        if not choice in func_dic: continue
        func_dic[choice]()
