# -*- coding utf-8 -*-

"""
@author:yankerp
@url:www.yankerphub.com
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Student('egon', 18)
print(obj.name, obj.age)