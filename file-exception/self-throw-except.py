#!/usr/bin/python3


class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as err:
    print('My Exception occurred, value: ', err.value)
