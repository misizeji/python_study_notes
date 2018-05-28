#!/usr/bin/python3


import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('can not open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()