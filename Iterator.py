#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable, Iterator


def g():
    yield 1
    yield 2
    yield 3

print('Iterator? 123:', isinstance(123, Iterator))