#!/usr/local/bin/python
#-*- coding: utf-8 -*-

class Person:
    __secret = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__secret = "I am Ricol and I love Lisa! Haha~~"

    def __str__(self):
        return "name: " + self.name + "; age: " + str(self.age) + "; secret: " + self.__secret

p = Person('ricol wang', 34)
print(p)

print("p isinstance Person -> " + str(isinstance(p, Person)))