#!/usr/bin/python3
def printinfo( arg1, *vartuple ):
    print("output: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return

# call printinfo method
printinfo(10)
printinfo(70, 60, 50)