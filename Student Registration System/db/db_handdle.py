# 数据处理层
import os, pickle
from conf import settings


def save(self):
    cls_name = self.__class__.__name__.lower()
    obj_path = os.path.join(settings.DB_PATH, cls_name)
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    user_path = os.path.join(obj_path,self.name)
    with open(user_path, 'wb')as f:
        pickle.dump(self, f)
        f.flush()


def select(cls, name):
    cls_name = cls.__name__.lower()
    obj_path = os.path.join(settings.DB_PATH, cls_name)
    if not os.path.exists(obj_path):
        os.mkdir(obj_path)
    user_path = os.path.join(obj_path, name)
    if not os.path.exists(user_path):
        return False
    with open(user_path, 'rb')as f:
        user_obj= pickle.load(f)
        if user_obj:
            return user_obj
        return False
