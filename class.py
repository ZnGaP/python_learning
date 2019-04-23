#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')


def run_twice(Animal):
    Animal.run()
    Animal.run()

class Timer(object):
    def run(self):
        print('start...')

run_twice(Timer())