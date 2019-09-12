#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import threading
from time import ctime
from time import sleep

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(2)

threads = []
t1 = threading.Thread(target=music, args=('Godspeed', ))
threads.append(t1)
t2 = threading.Thread(target=move, args=('Interstellar', ))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

	print("all over %s" % ctime())