#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2014

from sys import argv

def calcArea(line):
	dims = line.split("x")
	dims = map(int, dims)
	if len(dims) != 3: return 0
	l = dims[0]
	w = dims[1]
	h = dims[2]
	myDims = [ 2 * l * w, 2 * l * h, 2 * w * h]
	slack = min(myDims) / 2
	total = sum(myDims) + slack
	return total

dim = open("a2_input.txt", 'r')

toOrder = 0
while True:
	x = dim.readline().rstrip()
	if not x: break
	toOrder += calcArea(x)

print toOrder
