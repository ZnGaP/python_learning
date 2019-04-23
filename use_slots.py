#!\usr\bin\env python3
# -*- coding: utf-8 -*-

class Student(object):
    __slots__  = ('name', 'age')

class GraduateStudent(Student):
    pass

s = Student()
s.name = 'Michal'
s.age = 20

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError: ', e)

g = GraduateStudent()
g.score = 99
print(g.score)
