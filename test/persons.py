#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import random

def iis(flag, value1, value2):
    if flag: return value1
    return value2

class Being:
    COUNT = 0

    def __init__(self, name):
        self.name = name
        Being.COUNT += 1

    def __str__(self):
        return "name: %s" % self.name

class Person(Being):
    PERSON_COUNT = 0
    MALE = 1
    FEMALE = 0

    def __init__(self, name, age, gender):
        super(Person, self).__init__(name)
        self.age = age
        self.gender = gender
        Person.PERSON_COUNT += 1

    def __str__(self):
        return super.__str__(self) + ", age: %d, gender: %s" % (self.age, iis(self.gender == Person.MALE, 'male', 'female'))

class Animal(Being):
    ANIMAL_COUNT = 0

    def __init__(self, name, type):
        super(Animal, self).__init__(name)
        self.type = type
        Animal.ANIMAL_COUNT += 1

    def __str__(self):
        return super.__str__(self) + ", type: %s" % self.type

if __name__ == "__main__":
    being = []
    for i in range(10):
        if random.randint(0, 10) > 5:
            #create Person
            p = Person('ricol', 36, Person.MALE)
            being.append(p)
        else:
            #create Animal
            a = Animal('my cat', 'cat')
            being.append(a)
    for b in being:
        print(b)