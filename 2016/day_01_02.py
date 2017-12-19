#!/usr/bin/env python

# USAGE: a1a_grid_stepping.py
# Michael Chambers, 2015

import sys
import math

def log(*msg):
	print("LOG: ", *msg, file = sys.stderr)

myFile = "a1a_input.txt"
myFH = open(myFile, 'r')

dirString = myFH.read().rstrip()

dirs = dirString.split(", ")

startx = 0.0
starty = 0.0

startdir = math.radians(0)

allx = list()
ally = list()

for d in dirs:
	log("d ", d)
	myDir = d[0]
	myDistance = int(d[1:])
	if myDir == "R":
		startdir = startdir + ( math.pi / 2 )
	else:
		startdir = startdir - ( math.pi / 2 )
	log("startx ", startx)
	log("starty ", starty)
	log("myDistance ", myDistance)
	log("startdir ", startdir)
	startx = int(startx + myDistance * math.cos(startdir))
	starty = int(starty + myDistance * math.sin(startdir))

	for x,y in zip(allx,ally):
		if startx == x and starty == y:
			print("Solution: ", abs(startx) + abs(starty))

	allx.append(startx)
	ally.append(starty)


print("x: ", startx, " y: ", starty, " Total: ", abs(startx) + abs(starty))

