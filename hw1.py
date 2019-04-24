#!/usr/bin/python

import sys

args = sys.argv[1:]

for arg in args:
     f = open(arg, 'r')
     message = f.read()
     print(message)
     f.close()
