#!/usr/bin/env python

# USAGE: a8_analysis.py
# Michael Chambers, 2015
from __future__ import print_function

myFile = "a8_input.txt"
myFH = open(myFile, 'r')

rawTotal = 0
proTotal = 0
while True:
	line = myFH.readline().rstrip()
	if not line: break
	rawTotal += len(line)
	proTotal += len(eval(line))

difTotal = rawTotal - proTotal
print("Raw char: ", rawTotal, "\nInterp total: ", proTotal, "\nDifference: ", difTotal)
