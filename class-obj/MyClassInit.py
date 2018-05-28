#!/usr/bin/python3


class Complex:
    def __init__(self, realpart, imagpart):
        self.realpart = realpart
        self.imagpart = imagpart

x = complex(3.0, -4.5)
print(x.real, x.imag)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()
