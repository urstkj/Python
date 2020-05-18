#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print("Parent.__init__()...")

   def parentMethod(self):
      print('Parent.parentMethod()...')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
       super().__init__()
       print("Child.__init__()...")

   def childMethod(self):
      print('Child.childMethod()...')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method