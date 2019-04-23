#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-

from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key = str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def sort1(a):
    return len(a[0]) and a[0][:1]

print(sorted(students, key = sort1))