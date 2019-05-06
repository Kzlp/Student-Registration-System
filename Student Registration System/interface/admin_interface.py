# 管理员接口
from db import model
from lib import common
logger = common.get_logger('管理员')
# 创建学校
def creat_school(admin_name,school_name,school_addr):
    school_obj = model.School.select(school_name)
    if not school_obj:
        admin_obj = model.Admin.select(admin_name)
        admin_obj.creat_school(school_name,school_addr)
        info = '%s管理员注册%s学校'%(admin_name,school_name)
        logger.info(info)
        return True,'%s注册成功'%school_name
    else:
        return False,'该学校已存在'

# 创建老师
def creat_teacher(admin_name,teacher_name,teacher_pwd):
    teacher_obj = model.Teacher.select(teacher_name)
    if not teacher_obj:
        admin_obj = model.Admin.select(admin_name)
        admin_obj.creat_teacher(teacher_name,teacher_pwd)
        info = '%s管理员注册%s老师' % (admin_name, teacher_name)
        logger.info(info)
        return True,'%s老师注册成功'%teacher_name
    else:
        return False,'该老师已存在'

# 创建课程
def creat_course(admin_name,course_name,school_name):
    school_obj = model.School.select(school_name)
    if not school_obj:
        return '学校不存在！'
    admin_obj = model.Admin.select(admin_name)

    course_list = school_obj.check_school_course()
    if course_name not in course_list:
        admin_obj.creat_course(course_name)
        school_obj.school_course_list.append(course_name)
        school_obj.save()

        info = '%s管理员注册%s课程成功' % (admin_name, course_name)
        logger.info(info)
        return True,'%s课程创建成功！'% course_name
    else:
        return False,'课程重复！'
