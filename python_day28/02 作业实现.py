# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""


class School:
    """学校的类"""
    school_name = "Yankerp在线教育"

    def __init__(self, campus, addr, iphone):
        self.campus = campus
        self.addr = addr
        self.iphone = iphone
        self.classname = []

    def school_info(self):
        """输出学校基本信息"""
        print(f"{self.campus}")
        Class.tell_course()

    def add_class(self, clasname):
        """添加班级"""
        self.classname.append(clasname)

class Class:
    """这是班级的类"""

    def __init__(self, classname):
        self.classname = classname
        self.coursename = None

    def related_course(self, coursename):
        "关联课程"
        self.coursename = coursename

    def tell_course(self):
        print(self.classname, self.coursename)


ooob1 = School('11','222',3333)
ooob1.school_info()

obj1 = Class("脱产11期")
obj2 = Class("脱产12期")
