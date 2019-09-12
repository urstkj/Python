#!/usr/local/bin/python
#-*- coding: utf-8 -*-

class TestCompare(object):
    def __lt__(self, other):
        return "aaa"

t = TestCompare()
print(t < 1)
