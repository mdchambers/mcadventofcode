#!/usr/bin/env python

# USAGE: day_04_01.py
# Michael Chambers, 2015


inputfile = "day_04_input.txt"
fh = open(inputfile, 'r')

validpwd = 0
for line in fh:
	valid = True
	line = line.rstrip()
	words = line.split(" ")
	for pos1, w in enumerate(words):
		for pos2, x in enumerate(words):
			if pos1 == pos2:
				break
			if w == x:
				print("Matched {} to {}".format(w,x))
				valid = False
				break
	if valid:
		validpwd += 1

print("Part 1: Valid passwords: {}".format(validpwd))

fh.close()

### Part 2
from collections import Counter

inputfile = "day_04_input.txt"
fh = open(inputfile, 'r')

validpwd = 0
for line in fh:
	valid = True
	line = line.rstrip()
	words = line.split(" ")
	for pos1, w in enumerate(words):
		for pos2, x in enumerate(words):
			if pos1 == pos2:
				break
			wcounter = Counter(w)
			xcounter = Counter(x)
			if wcounter == xcounter:
				print("Matched {} to {}".format(w,x))
				valid = False
				break
	if valid:
		validpwd += 1

print("Part 2: Valid passwords: {}".format(validpwd))

