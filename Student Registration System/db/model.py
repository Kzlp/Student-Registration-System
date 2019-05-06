from db import db_handdle


class BaseClass:
    def save(self):
        db_handdle.save(self)

    @classmethod
    def select(cls, name):
        res = db_handdle.select(cls, name)
        if not res:
            return False
        return res


class Admin(BaseClass):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def creat_school(self, school_name, school_addr):
        School(school_name,school_addr)

    def creat_teacher(self, teacher_name, teacher_pwd, ):
        Teacher(teacher_name,teacher_pwd)

    def creat_course(self,course_name):
        Course(course_name)



class Student(BaseClass):
    def __init__(self,student_name,student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.student_course_list = []
        self.score = {}
        self.save()

    def choice_school(self,school_name):
        self.school = school_name
        self.save()
    def check_student_school(self,student_name):
        student_obj = Student.select(student_name)
        return student_obj.school
    def check_school_course(self,school_name):
        school_obj = School.select(school_name)
        return school_obj.school_course_list
    def choice_course(self,course_name):
        self.student_course_list.append(course_name)
        self.score[course_name] = 0
        self.save()
    def check_student_course(self):
        return self.student_course_list
    def check_score(self,course_name):
        return self.score[course_name]


class Teacher(BaseClass):
    def __init__(self,teacher_name,teacher_pwd):
        self.name =teacher_name
        self.pwd = teacher_pwd
        self.teacher_course_list = []
        self.save()
    def check_course(self):
        return self.teacher_course_list

    def choice_course(self,course_name):
        self.teacher_course_list.append(course_name)
        self.save()

    def check_course_student(self,course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list
    def change_student_score(self,course_name,student_name,score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()
class School(BaseClass):
    def __init__(self,school_name,school_addr):
        self.name = school_name
        self.addr = school_addr
        self.school_course_list = []
        self.save()
    def check_school_course(self):
        return self.school_course_list

class Course(BaseClass):
    def __init__(self,course_name):
        self.name = course_name
        self.student_list = []
        self.save()
    def add_student(self,student_name):
        self.student_list.append(student_name)
        self.save()