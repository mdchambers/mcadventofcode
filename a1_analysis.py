#!/usr/bin/env python

# USAGE: a1_analysis.py
# Michael Chambers, 2015

myFile = "a1_input.txt"
myFH = open(myFile)

dirs = myFH.read().rstrip()

up = dirs.count('(')
down = dirs.count(')')

final = up - down

print "Final floor: %d" % final