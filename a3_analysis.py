#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2015
import itertools

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

print("Total moves:", len(moves), "\nUnique houses:", len(positions))


## Part 2

mfh = open("a3_input.txt", 'r').read().rstrip()

sanX = 0
sanY = 0
robX = 0
robY = 0

spos = set("0 0")
rpos = set("0 0")

def getMove(x, y, d):
	if d == ">":
		x += 1
	elif d == "<":
		x -= 1
	elif d == "^":
		y += 1
	elif d == "v":
		y -= 1
	return(x,y)

def pairs(x):
	if len(x) % 2 != 0:
		x.append(None)
	p1 = itertools.islice(x, 0, None, 2)
	p2 = itertools.islice(x, 1, None, 2)
	return(zip(p1, p2))

positions = set()
for i in pairs(mfh):
	sanX, sanY = getMove(sanX, sanY, i[0])
	pos =  "%d %d" % (sanX, sanY)
	positions.add(pos)
	if i[1]:
		robX, robY = getMove(robX, robY, i[1])
		pos =  "%d %d" % (robX, robY)
		positions.add(pos)
print("Total rob/san houses: ", len(positions))

