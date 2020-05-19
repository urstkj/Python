#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def isSorted(data):
    for i in range(1, len(data)):
        if data[i - 1] > data[i]: return False
    return True

def isHeap(data, index):
    l = index * 2 + 1
    r = l + 1
    if l < len(data):
        if data[index] < data[l]: return False
        if not isHeap(data, l): return False
    if r < len(data):
        if data[index] < data[r]: return False
        if not isHeap(data, r): return False
    return True