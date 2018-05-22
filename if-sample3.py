#!/usr/bin/python3

num  = int(input("please input a number: "))
if num %2 == 0:
    if num %3 == 0:
        print("the number you input can be divide by 2 and 3")
    else:
        print("the number you input can not be divide by 3 but 2")
else:
    if num %3 == 0:
        print("the number you input can not be divide by 2 but 3")
    else:
        print("the number you input can not be divide by 2 and 3")
