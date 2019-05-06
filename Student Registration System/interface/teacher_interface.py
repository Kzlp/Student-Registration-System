# 教师接口
from db import model
from interface import common_interface
from lib import common
logger = common.get_logger('教师')

def check_teacher_course(teacher_name):
    '获取老师的课程信息'
    teacher_obj = model.Teacher.select(teacher_name)
    course_list = teacher_obj.check_course()
    if not course_list:
        return False
    return course_list
def get_course_list(file_name):
    '获取所有课程'
    course_list = common_interface.get_file(file_name)
    if not course_list:
        return False
    return course_list
def choice_coures_interface(teacher_name,course_name):
    '老师选择课程'
    teacher_obj = model.Teacher.select(teacher_name)
    course_list = teacher_obj.check_course()
    if course_name not in course_list:
        teacher_obj.choice_course(course_name)
        info = '%s老师选择%s课程'%(teacher_name,course_name)
        logger.info(info)
        return True,'课程添加成功'
    return False,'该课程已存在'

def check_course_student_interface(teacher_name,course_name):
    '查看课程下学生'
    teacher_obj = model.Teacher.select(teacher_name)
    student_list = teacher_obj.check_course_student(course_name)
    if not student_list:
        return False
    return student_list
def change_student_score_interface(teacher_name,course_name,student_name,score):
    '修改课程下学生成绩'
    teacher_obj = model.Teacher.select(teacher_name)
    teacher_obj.change_student_score(course_name,student_name,score)
    info = '%s老师修改%s学生%s课程分数为%s' % (teacher_name, student_name,course_name,score)
    logger.info(info)
    return '修改成功'