#!/usr/bin/env python

# USAGE: day_19_01.py
# Michael Chambers, 2017

import re
import numpy as np

class Grid:
	def __init__(self, file, initialvecx = 1, initialvecy = 0):
		self.cells = list()
		self.vecx = initialvecx
		self.vecy = initialvecy
		self.outputstring = ""
		with open(file, 'r') as fo:
			for line in fo:
				line = line.rstrip("\n")
				self.cells.append(list(line))
		self.cells = np.array(self.cells)
		self.findStart()


	def findStart(self):
		self.posx = 0
		self.posy = np.where(np.isin(self.cells[0], "|"))[0][0]


	def traverse(self):
		# start = self.findStart()
		currchar = self.cells[self.posx,self.posy]
		print("Pos: {}, {} Cell: {} Vec: {} {} Output:".format(self.posx, self.posy, currchar, self.vecx, self.vecy, self.outputstring))
		if currchar == " ":
			print("ERROR: left track")
			return(False)
		elif currchar == "+":
			self.switchDirection()
		if re.match(r"[A-Z]", currchar):
			print("Adding char")
			self.outputstring += currchar
		self.posx += self.vecx
		self.posy += self.vecy
		return(True)

	def switchDirection(self):
		print("At junction")
		currchar = self.cells[self.posx,self.posy]
		if self.vecx != 0:
			print("Switch to yvec")
			self.vecx = 0
			if self.posy + 1 < self.cells.shape[1]:
				if self.cells[self.posx, self.posy + 1] == "-" or re.match(r"[A-Z]", self.cells[self.posx, self.posy + 1]):
					self.vecy = 1
			if self.posy - 1 >= 0:
				if self.cells[self.posx, self.posy - 1] == "-" or re.match(r"[A-Z]", self.cells[self.posx, self.posy - 1]):
					self.vecy = -1
		elif self.vecy != 0:
			print("Switch to xvec")
			self.vecy = 0
			if self.posx + 1 < self.cells.shape[0]:
				if self.cells[self.posx + 1, self.posy] == "|" or re.match(r"[A-Z]", self.cells[self.posx + 1, self.posy]):
					self.vecx = 1
			if self.posx - 1 >= 0:
				if self.cells[self.posx - 1, self.posy] == "|" or re.match(r"[A-Z]", self.cells[self.posx - 1, self.posy]):
					self.vecx = -1

	def printGrid(self, x, y):
		toprint = self.cells[:x][:y]
		outstr = ""
		for i in toprint:
			for j in i:
				outstr += j
			outstr += "\n"
		print(outstr)

# class Cell:
# 	def __init__(self, char):
# 		self.char = char


def main():
	file = "day_19_input.txt"
	# file = "day_19_testinput.txt"
	g = Grid(file)
	# g.printGrid(10, 10)
	print(g.cells)
	# print(type(g.cells))
	# print(g.cells.shape)
	steps = 0
	while g.traverse():
		steps += 1
	print("String: {} Steps: {}".format(g.outputstring, steps))



if __name__ == "__main__":
	main()

