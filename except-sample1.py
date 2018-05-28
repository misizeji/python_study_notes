#!/usr/bin/python3


while True:
    try:
        x = int(input("please input a number: "))
        break
    except ValueError:
        print("Opps, that was not a valid number. Try again ")