#!/usr/bin/python3

# Fibonacci series  斐波那契数列
# 两个元素的总和确定了下一个数

a, b = 0, 1
c = 0

while b < 10:
    print(b)
#    a, b = b, a+b
# 以上一行等效语句如下：
    c = a + b
    a = b
    b = c