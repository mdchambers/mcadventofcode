#!/usr/bin/env python

# USAGE: day_08_01.py
# Michael Chambers, 2017

import numpy as np

class Screen():
	def __init__(self):
		self.grid = np.zeros((6, 50))


	def processCommands(self, file):
		with open(file, 'r') as fo:
			for line in fo:
				line = line.rstrip()
				ls = line.split(" ")
				# print(ls)
				if ls[0] == "rect":
					a, b = ls[1].split("x")
					a = int(a)
					b = int(b)
					self.rect(b, a)
				elif ls[1] == "row":
					row = int(ls[2].split("=")[1])
					pixel = int(ls[4])
					self.rotateRow(row, pixel)
				elif ls[1] == "column":
					col = int(ls[2].split("=")[1])
					pixel = int(ls[4])
					self.rotateCol(col, pixel)

	def rect(self, x, y):
		print("Rect: {} {} ".format(x, y))
		self.grid[:x,:y] = 1

	def rotateRow(self, row, pixel):
		print("Rot row: {} {} ".format(row, pixel))
		startrow = self.grid[row,]
		newrow = np.concatenate((startrow[len(startrow) - pixel:], startrow[:len(startrow) - pixel]))
		self.grid[row] = newrow

	def rotateCol(self, col, pixel):
		print("Rot col: {} {} ".format(col, pixel))
		startcol = self.grid[:,col]
		newcol = np.concatenate((startcol[len(startcol) - pixel:], startcol[:len(startcol) - pixel]))
		self.grid[:,col] = newcol

	def countOn(self):
		return(np.count_nonzero(self.grid))

	def __repr__(self):
		outstr = ""
		for row in self.grid:
			for cell in row:
				# print(cell)
				if cell == 1:
					outstr += "*"
				else:
					outstr += " "
			outstr += "\n"
		return(outstr)

def main():
	file = "day_08_input.txt"
	# file = "day_08_test.txt"

	s = Screen()
	s.processCommands(file)
	print("On: {}".format(s.countOn()))
	print(s)
	# UPOJFLBCEZ

if __name__ == "__main__":
	main()

