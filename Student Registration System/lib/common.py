# 公用模块
import logging.config
from conf import settings

# 获取日志
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger

# 用户登录装饰器
def auth(type_name):
    from cose import admin,student,teacher
    def wrap(func):
        def inner(*args,**kwargs):
            if type_name == 'admin':
                if admin.admin_login_info['name']:
                    return func(*args,**kwargs)
                else:
                    print('请先登录！')
                    admin.login()
            elif type_name == 'student':
                if student.student_login_info['name']:
                    return func(*args,**kwargs)
                else:
                    print('请先登录！')
                    student.login()
            elif type_name == 'teacher':
                if teacher.teacher_login_info['name']:
                    return func(*args,**kwargs)
                else:
                    print('请先登录！')
                    teacher.login()
        return inner
    return wrap