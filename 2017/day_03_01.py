#!/usr/bin/env python

# USAGE: day_03_01.py
# Michael Chambers, 2015
from collections import defaultdict


# Defines each square in the grid based on square shell number
class Square(object):
	def __init__(self, n):
		self.sqnum = n
		self.sqmin = self.minInSquare()
		self.sqmax = self.maxInSquare()
		self.sqsides = 1 + 2 * n

	# Returns the position of a given value within the square
	def getPos(self, v):
		topright = self.sqmin + self.sqsides -2
		topleft = topright + self.sqsides - 1
		bottomleft = topleft + self.sqsides - 1
		bottomright = bottomleft + self.sqsides - 1

		if(v <= topright):
			x = self.sqnum
			y = self.sqnum - (topright - v)
		elif(v <= topleft):
			x = (topleft - v) - self.sqnum
			y = self.sqnum
		elif(v <= bottomleft):
			x = -self.sqnum
			y = (bottomleft - v) - self.sqnum
		else:
			x = self.sqnum - (bottomright - v)
			y = -self.sqnum
		pos = (x,y)
		return(pos)
	
	def numsInSquare(self):
		return(8 * self.sqnum)

	def minInSquare(self):
		return(sum(8 * i for i in range(self.sqnum)) + 2)

	def maxInSquare(self):
		return(self.sqmin + self.numsInSquare() - 1)

	# Returns a list of all positions within the square
	def getAllPos(self):
		allpos = list()
		for i in range(self.sqmin, self.sqmax + 1):
			allpos.append(self.getPos(i))
		return(allpos)

### Part 1
# Find square containing number
minput = 347991

nsq = 1
while True:
	tmpsquare = Square(nsq)
	if(tmpsquare.minInSquare() <= minput and tmpsquare.maxInSquare() >= minput):
		break
	else:
		nsq += 1

inSquare = Square(nsq)
mypos = inSquare.getPos(minput)
mydist = sum(map(abs, mypos))
print("Square: ", nsq)
print("Pos: ", mypos)
print("Distance: ", mydist)

### Part 2

# Defines and generates a grid
class Grid(object):
	def __init__(self):
		self.cells = defaultdict( lambda: 0)
		self.cells[(0,0)] = 1

	def generate(self, maxvalue):
		sqnum = 1
		overmax = False
		while not overmax:
			# print("Doing square {}".format(sqnum))
			square = Square(sqnum)
			for cell in square.getAllPos():
				adjvals = self.getAdjacentSum(cell)
				# print("putting val {} in cell {}".format(adjvals, cell))
				self.cells[cell] = adjvals
				# print("Cell value: {}".format(adjvals))
				if(self.cells[cell] > maxvalue):
					overmax = True
			sqnum += 1

	def getMaxCell(self):
		maxval = max(self.cells.values())
		for k, v in self.cells.items():
			if v == maxval:
				maxpos = k
		return("Max value {} in cell {}".format(maxval, maxpos))

	def getMaxOverLimit(self, mylim):
		overVal = min([x for x in self.cells.values() if x > mylim])
		for k, v in self.cells.items():
			if v == overVal:
				overPos = k
		return(overPos)

	
	def getAdjacentSum(self, cellPos):
		adjvals = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				posij = (cellPos[0] - i, cellPos[1] - j)
				# print("for pos {} val {}".format(posij, self.cells[posij]))
				adjvals += self.cells[posij]
		return(adjvals) 


myg = Grid()
myg.generate(minput)
print("Max cell: ", myg.getMaxCell())
outpos = myg.getMaxOverLimit(minput)
outval = myg.cells[outpos]
print("Max over limit: {} in cell: {}".format(outval, outpos))




# class Cell(object):
# 	def __init__(self, x, y, value):
# 		self.x = x
# 		self.y = y
# 		self.value = value

# 	def getValue(self):
# 		return(value)

# 	def getDistance(self):
# 		return(abs(self.x) + abs(self.y))




