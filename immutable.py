#!/usr/bin/python3

# could wirte method explain
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("list value: ", mylist)
    return

mylist = [10, 20, 30]
changeme(mylist)
print("list value: ",mylist)