#!/usr/bin/env python

# USAGE: day_05_01.py
# Michael Chambers, 2015

file = "day_05_input.txt"
fh = open(file, 'r')

offsets = list()
for line in fh:
	off = int(line)
	offsets.append(off)
fh.close()

inBounds = True
jumps = 0
position = 0
while True:
	jumps += 1
	nextpos = position + offsets[position]
	if nextpos >= (len(offsets)) or nextpos < 0:
		print("left offsets to {} after {} jumps".format(nextpos, jumps))
		break
	offsets[position] += 1
	position = nextpos


## Part 2

file = "day_05_input.txt"
fh = open(file, 'r')

offsets = list()
for line in fh:
	off = int(line)
	offsets.append(off)

inBounds = True
jumps = 0
position = 0
while True:
	jumps += 1
	nextpos = position + offsets[position]
	if nextpos >= (len(offsets)) or nextpos < 0:
		print("left offsets to {} after {} jumps".format(nextpos, jumps))
		break
	if offsets[position] >= 3:
		offsets[position] -= 1
	else:
		offsets[position] += 1
	position = nextpos




