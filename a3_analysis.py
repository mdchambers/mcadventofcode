#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2015

myFile = open("a3_input.txt", 'r').read()

xcur = 0
ycur = 0

positions = set()
moves = list(myFile)
for i in moves:
	if i == ">":
		xcur += 1
	elif i == "<":
		xcur -= 1
	elif i == "^":
		ycur += 1
	elif i == "v":
		ycur -= 1
	pos =  "%d %d" % (xcur, ycur)
	positions.add(pos)
	# print pos

print "Total moves: %d\nUnique houses: %d" % (len(moves), len(positions))



