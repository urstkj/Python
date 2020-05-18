#!/usr/local/bin/python

import random

def quick_sort(data):
    if len(data) <= 1: return data
    m = len(data) / 2
    pivot = data[m]
    left, right = [], []
    for i in range(len(data)):
        if i == m: continue
        if data[i] < pivot: left.append(data[i])
        else: right.append(data[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

LEN = int(1e6)
print 'generating...'
data = [random.randint(0, LEN) for _ in range(LEN)]
print 'sorting...'
sorted = quick_sort(data)
print 'done.'