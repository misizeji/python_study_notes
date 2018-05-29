#!/usr/bin/python3


class Parent:

    def mymethod(self):
        print(" call farther's method ")


class Child(Parent):

    def mymethod(self):
        print(" call child's method ")

c = Child()
c.mymethod()
super(Child, c).mymethod()