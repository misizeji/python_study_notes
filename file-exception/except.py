#!/usr/bin/python3


def devide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("devision by zero!")
    else:
        print("result: ", result)
    finally:
        print("executing finally clause")

devide(2, 1)

devide(2, 0)

devide('2', '1')