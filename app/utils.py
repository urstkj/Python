#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import dis

def sum():
    vara = 10
    varb = 20

    sum = vara + varb
    print("vara + varb = %d" % sum)

# Call dis function for the function.

dis.dis(sum)
