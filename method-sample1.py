#!/usr/bin/python3

def area(width, height):
    return width * height

def welcome(name):
    print("welcome",name)

welcome("Runoob")

w, h = 4, 5
print("width =", w, "height =", h, "area =",area(w, h))
