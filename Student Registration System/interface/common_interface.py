# 公共接口
import os
from conf import settings
from db import model
from lib import common
logger = common.get_logger('用户')
# 注册接口
def register_interface(type_name, name, pwd):
    if type_name == 'admin':
        res = model.Admin.select(name)
        if res:
            return False, '用户已存在'
        else:
            model.Admin(name, pwd)
            info = '%s注册为管理员账号'%name
            logger.info(info)
            return True, '注册成功'
    else:
        res = model.Student.select(name)
        if res:
            return False, '用户已存在'
        else:
            model.Student(name, pwd)
            info = '%s注册为学生账号' % name
            logger.info(info)
            return True, '注册成功'
# 登录接口
def login_interface(type_name, name, pwd):
    if type_name == 'admin':
        res = model.Admin.select(name)
        if not res:
            return False, '用户不存在'
        else:
            if res.pwd != pwd:
                return False, '密码错误'
            else:
                info = '管理员%s登录账号' % name
                logger.info(info)
                return True, '登录成功'
    elif type_name == 'student':
        res = model.Student.select(name)
        if not res:
            return False, '用户不存在'
        else:
            if res.pwd != pwd:
                return False, '密码错误'
            else:
                info = '学生%s登录账号' % name
                logger.info(info)
                return True, '登录成功'
    elif type_name == 'teacher':
        res = model.Teacher.select(name)
        if not res:
            return False, '用户不存在'
        else:
            if res.pwd != pwd:
                return False, '密码错误'
            else:
                info = '老师%s登录账号' % name
                logger.info(info)
                return True, '登录成功'
# 获取文件资源
def get_file(file_name):
    file_path = os.path.join(settings.DB_PATH,file_name)
    if not os.path.exists(file_path):
        return False,'暂无信息！'
    return os.listdir(file_path)

