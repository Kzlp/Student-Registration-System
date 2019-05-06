# 教师视图
teacher_login_info = {'name':None}
from interface import common_interface,teacher_interface



def login():
    '登录'
    while True:
        if teacher_login_info['name']:
            print('用户已登录')
            break
        name = input('输入登录名(q\exit)>>:')
        if name == 'q': break
        if not name: continue
        pwd = input('输入密码>>:')
        flag, msg = common_interface.login_interface('teacher', name, pwd)
        if flag:
            print(msg)
            teacher_login_info['name'] = name
            break
        else:
            print(msg)
def check_course():
    '查看课程'
    course_list = teacher_interface.check_teacher_course(teacher_login_info['name'])
    if not course_list:
        print('暂无课程信息')
    else:
        print(course_list)

def choice_course():
    '选择课程'
    while True:
        course_list = teacher_interface.get_course_list('course')
        if not course_list:
            print('暂无课程信息')
            continue
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
        flag, msg = teacher_interface.choice_coures_interface(teacher_login_info['name'],course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
def check_student():
    '查看学生'
    while True:
        teacher_course_list = teacher_interface.check_teacher_course(teacher_login_info['name'])
        if not teacher_course_list:
            print('请先选择教授课程！')
            break
        for k, v in enumerate(teacher_course_list):
            print(k, v)
        choice = input('请输入课程编号(q\exit)>>:')
        if choice == 'q': break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(teacher_course_list)):
            print('输入有误！')
            continue
        course_name = teacher_course_list[choice]
        student_list= teacher_interface.check_course_student_interface(teacher_login_info['name'], course_name)
        if not student_list:
            print('该课程下暂无学生')
            break
        else:
            print(student_list)
            break
def alter_score():
    '修改分数'
    while True:
        teacher_course_list = teacher_interface.check_teacher_course(teacher_login_info['name'])
        if not teacher_course_list:
            print('请先选择教授课程！')
            break
        for k, v in enumerate(teacher_course_list):
            print(k, v)
        choice = input('请输入课程编号(q\exit)>>:')
        if choice == 'q': break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(teacher_course_list)):
            print('输入有误！')
            continue
        course_name = teacher_course_list[choice]
        student_list= teacher_interface.check_course_student_interface(teacher_login_info['name'], course_name)
        if not student_list:
            print('该课程下暂无学生')
            break
        for k, v in enumerate(student_list):
            print(k, v)
        choice = input('请输入学生编号(q\exit)>>:')
        if choice == 'q': break
        if not choice.isdigit():
            print('请输入正确数字！')
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(student_list)):
            print('输入有误！')
            continue
        student_name = student_list[choice]
        choice_score = input('请输入修改分数(q\exit)>>:')
        if choice_score == 'q':break
        flag = teacher_interface.change_student_score_interface(teacher_login_info['name'], course_name,student_name,choice_score)
        if flag:
            print(flag)
            break
func_dic = {
    '1': login,
    '2': check_course,
    '3': choice_course,
    '4': check_student,
    '5': alter_score,
}


def teacher_sys():
    '启动'
    while True:
        choice = input('''
-------------教师管理系统--------------
    1 登录
    2 查看课程
    3 选择课程
    4 查看学生
    5 修改分数
    0 退出
选择操作 >>:  ''')
        if not choice.isdigit():
            print('请输入数字编号！')
            continue
        if choice == '0': break
        if not choice in func_dic: continue
        func_dic[choice]()
