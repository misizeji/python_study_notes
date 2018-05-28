#!/usr/bin/python3


import sys


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS Error: {0}".format(err))
except ValueError:
    print("Could not convert data to integer.")
except:
    print("Unexcept error:", sys.exc_info()[0])
    raise
