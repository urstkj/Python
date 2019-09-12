#!/usr/local/bin/python
#-*- coding: utf-8 -*-

def isPrime(num):
    isPrime = True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            isPrime = False
            break
    return isPrime

for num in range(2, 100):
    if isPrime(num):
        print("%d\t" % num, end='')

print("\n")