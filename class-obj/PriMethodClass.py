#!/usr/bin/python3


class Site:
    def __init__(self, name, url):
        self.name = name        # public
        self.__url = url        # private

    def who(self):
        print('name: ', self.name)
        print('url: ',self.__url)

    def __foo(self):            # private method
        print("this is a private method")

    def foo(self):              # common method
        print("this is a common method")
        self.__foo()

x = Site('NewBird teach lesson', 'www.runoob.com')
x.who()
x.foo()
# report an error
# x.__foo()