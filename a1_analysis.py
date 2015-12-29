#!/usr/bin/env python

# USAGE: a1_analysis.py
# Michael Chambers, 2015

myFile = "a1_input.txt"
myFH = open(myFile)

dirs = myFH.read().rstrip()

up = dirs.count('(')
down = dirs.count(')')

final = up - down

print("Final floor:", final)

## Part 2

myFile = "a1_input.txt"
myFH = open(myFile)

dirs = myFH.read().rstrip()

floor = 0
for idx in range(len(dirs)):
	val = dirs[idx]
	if val == "(":
		floor += 1
	if val == ")":
		floor -= 1
	if floor == -1:
		print("Hit -1: ", idx + 1, val)
