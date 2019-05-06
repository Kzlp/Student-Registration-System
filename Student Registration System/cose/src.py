# 主程序
from cose import admin,student,teacher

func_dic = {
    '1':student.student_sys,
    '2':teacher.teacher_sys,
    '3':admin.admin_sys,
}

def run():
    '主程序启动'
    while True:
        choice = input('''
-----------欢迎进入选课系统-----------
1 学生视图
2 教师视图
3 管理员视图
0 退出
选择操作 >>: ''')

        if not choice.isdigit():
            print('请输入数字编号！')
            continue
        if choice == '0': break
        if not choice in func_dic: continue
        func_dic[choice]()

