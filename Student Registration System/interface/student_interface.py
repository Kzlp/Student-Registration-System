# 学生接口
from db import model
from lib import common
logger = common.get_logger('学生')

def choice_school_interface(student_name,school_name):
    '选择学校'
    school_obj = model.School.select(school_name)
    if not school_obj:
        return False,'暂无学校'
    student_obj = model.Student.select(student_name)
    student_obj.choice_school(school_name)
    info = '%s同学选择%s学校成功'%(student_name, school_name)
    logger.info(info)
    return True,info

def check_studene_school_interface(student_name):
    '获取学生学校信息'
    student_obj = model.Student.select(student_name)
    school_name = student_obj.check_student_school(student_name)
    if not school_name:
        return False
    return school_name

def check_school_course_interface(school_name):
    '获取学生学校课程信息'
    school_obj = model.School.select(school_name)
    course_list = school_obj.check_school_course()
    if not course_list:
        return False
    return course_list

def choice_course_interface(student_name,course_name):
    # '选择课程'
    student_obj = model.Student.select(student_name)
    course_list = student_obj.student_course_list
    if course_name in course_list:
        return False,'课程重复选择！'
    student_obj.choice_course(course_name)
    course_obj = model.Course.select(course_name)
    course_obj.add_student(student_name)
    return True,'%s课程添加成功！'%course_name

def get_student_course(student_name):
    '获取学生课程信息'
    student_obi = model.Student.select(student_name)
    if not student_obi.check_student_course():
        return False
    return student_obi.check_student_course()

def check_student_score(student_name,course_name):
    '查看学生课程分数'
    student_obi = model.Student.select(student_name)
    return student_obi.check_score(course_name)
