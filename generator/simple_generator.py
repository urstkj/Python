#!/usr/local/bin/python

def f():
	yield "f..."

def g():
	yield from f()

for i in g():
	print i

