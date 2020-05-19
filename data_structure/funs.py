#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def check(data):
    for i in range(1, len(data)):
        if data[i - 1] > data[i]: return False
    return True
