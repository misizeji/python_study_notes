#!/usr/bin/python3


s = 'Hello, Runoob'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'x的值为： ' + repr(s) + ', y的值为： ' + repr(y) + '...'
print(s)

# repr() 可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

# repr() 函数的参数可以是python的任何对象
print(repr((x, y, ('Google', 'Runoob'))))

