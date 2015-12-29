#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2014

from sys import argv

def calcArea(line):
	dims = line.split("x")
	dims = list(map(int, dims))
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

print("Paper: ", toOrder)

## Part 2

class Present(object):
	def __init__(self, width, height, length):
		self.width = width
		self.height = height
		self.length = length

	def getVolume(self):
		return self.width * self.height * self.length

	def getPerimeters(self):
		perm = list()
		perm.append( 2 * self.width + 2 * self.height)
		perm.append( 2 * self.width + 2 * self.length)
		perm.append( 2 * self.length + 2 * self.height)
		return(perm)

	def ribbon(self):
		return( self.getVolume() + min(self.getPerimeters()))

mfh = open("a2_input.txt", 'r')
toOrder = 0
while True:
	line = mfh.readline().rstrip()
	if not line: break
	ll = line.split("x")
	dims = list(map(int, ll))
	p = Present(dims[0], dims[1], dims[2])
	toOrder += p.ribbon()
print("Ribbon: ", toOrder)

