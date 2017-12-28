#!/usr/bin/env python

# USAGE: day_22_01.py
# Michael Chambers, 2017

class Grid:
	def __init__(self, startFile):
		# Load initial infected sites
		# Origin is top-left of input file
		self.infected = set()
		posx = 0
		with open(startFile, 'r') as fo:
			for i, line in enumerate(fo):
				line = line.rstrip()
				posx = int((len(line) -1) / 2)
				for j, char in enumerate(line):
					if char == "#":
						self.infected.add((i, j))

		# Set initial position to middle of start grid
		posy = int((sum(1 for line in open(startFile)) - 1) / 2)
		self.pos = (posx, posy)
		self.vec = (-1,0)
		self.infectionEvents = 0

	def update(self):
		if self.pos in self.infected:
			self.infected.remove(self.pos)
			self.turnRight()
		else:
			self.infectionEvents += 1
			self.infected.add(self.pos)
			self.turnLeft()
		self.pos = (self.pos[0] + self.vec[0], self.pos[1] + self.vec[1])

	def turnLeft(self):
		if self.vec == (-1, 0):
			self.vec = (0, -1)
		elif self.vec == (0, -1):
			self.vec = (1,0)
		elif self.vec == (1, 0):
			self.vec = (0, 1)
		else:
			self.vec = (-1, 0)

	def turnRight(self):
		if self.vec == (-1, 0):
			self.vec = (0, 1)
		elif self.vec == (0, 1):
			self.vec = (1, 0)
		elif self.vec == (1, 0):
			self.vec = (0, -1)
		else:
			self.vec = (-1, 0)


class ComplexGrid:
	# clean : 0
	# weakened : 1
	# infected : 2
	# flagged : 3

	def __init__(self, startFile):
		# Load initial infected sites
		# Origin is top-left of input file
		self.weakened = set()
		self.infected = set()
		self.flagged = set()
		posx = 0
		with open(startFile, 'r') as fo:
			for i, line in enumerate(fo):
				line = line.rstrip()
				posx = int((len(line) -1) / 2)
				for j, char in enumerate(line):
					if char == "#":
						self.infected.add((i, j))

		# Set initial position to middle of start grid
		posy = int((sum(1 for line in open(startFile)) - 1) / 2)
		self.pos = (posx, posy)
		self.vec = (-1,0)
		self.infectionEvents = 0

	def update(self):
		if self.pos in self.weakened:
			self.weakened.remove(self.pos)
			self.infected.add(self.pos)
			self.infectionEvents += 1
		elif self.pos in self.infected:
			self.infected.remove(self.pos)
			self.flagged.add(self.pos)
			self.turnRight()
		elif self.pos in self.flagged:
			self.flagged.remove(self.pos)
			self.reverse()
		else:
			self.weakened.add(self.pos)
			self.turnLeft()
		self.pos = (self.pos[0] + self.vec[0], self.pos[1] + self.vec[1])

	def turnLeft(self):
		if self.vec == (-1, 0):
			self.vec = (0, -1)
		elif self.vec == (0, -1):
			self.vec = (1,0)
		elif self.vec == (1, 0):
			self.vec = (0, 1)
		else:
			self.vec = (-1, 0)

	def turnRight(self):
		if self.vec == (-1, 0):
			self.vec = (0, 1)
		elif self.vec == (0, 1):
			self.vec = (1, 0)
		elif self.vec == (1, 0):
			self.vec = (0, -1)
		else:
			self.vec = (-1, 0)	

	def reverse(self):
		self.vec = tuple(-x for x in self.vec)	

def main():
	file = "day_22_input.txt"
	# file = "day_22_test.txt"
	g = Grid(file)
	# print(g.infected)
	# print("Pos {} Vec {}".format(g.pos, g.vec))
	for i in range(10000):
		g.update()
		# print(g.infected)
		# print("Pos {} Vec {}".format(g.pos, g.vec))
	print("Part 1: {}".format(g.infectionEvents))

	cg = ComplexGrid(file)
	for i in range(10000000):
		if i % 500000 == 0:
			print(i)
		cg.update()
	print("Part 2: {}".format(cg.infectionEvents))



if __name__ == "__main__":
	main()

