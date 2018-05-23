#!/usr/bin/python3

import sys

def fibonacci(n): # generator method
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f is a returned generator

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
