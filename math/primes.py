#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def primes(n):
    a, b = 2, 3
    data = []
    c = b
    while c < n:
        c = a * b + 1
        a = b
        b = c
        data.append(c)
    return data

N = 1e10
data = primes(N)
print(data)
