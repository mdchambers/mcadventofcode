#!/usr/bin/env python

# USAGE: day_21_01.py
# Michael Chambers, 2017

import sys
import numpy as np
from copy import copy
import time

class Artwork():
	def __init__(self, initialPattern, transformations):
		self.pattern = initialPattern
		self.trans = transformations
		self.divisions = 0

	def division(self):
		# If 3x3 input, handle initial transformation to 4x4
		if self.pattern.shape[0] == 3:
			# print("Initial tansformation")
			self.pattern = self.findTransformation(self.pattern)
			return()

		# Otherwise, split pattern into sections
		splitBy = 2 if self.pattern.shape[0] % 2 == 0 else 3
		subpatterns = np.split(self.pattern, self.pattern.shape[0] / splitBy, 0)
		subpatterns = list(map(lambda x: np.split(x, self.pattern.shape[1] / splitBy, 1), subpatterns))
		# subpatterns = [ item for sublist in subpatterns for item in sublist ]
		# for i, s in enumerate(subpatterns):
		# 	print("Subpattern {}\n{}".format(i, s))

		# For each subpattern
		outputPattern = np.array([])
		for subRow in subpatterns:
			outputRow = np.array([])
			for subCell in subRow:
				subTrans = self.findTransformation(subCell)
				outputRow = np.hstack([outputRow, subTrans]) if outputRow.size > 0 else subTrans
			outputPattern = np.vstack([outputPattern, outputRow]) if outputPattern.size > 0 else outputRow
		self.pattern = outputPattern
		return()

	def findTransformation(self, subpattern):
		matchingTrans = None
		for t in self.trans:
			if np.count_nonzero(t.init) != np.count_nonzero(subpattern) or t.init.size != subpattern.size:
				continue
			for p in t.permutations:
				if np.array_equal(subpattern, p):
					matchingTrans = t
					break
		if not matchingTrans:
			print("ERROR")
			sys.exit()
		return(matchingTrans.final)

	def countOn(self):
		return(np.count_nonzero(self.pattern))

	def __repr__(self):
		outstr = format(self.pattern)
		return(outstr)


class Transformation():
	def __init__(self, line):
		ls = line.split(" => ")
		self.init = patternToArray(ls[0])
		self.final = patternToArray(ls[1])
		self.permutations = self.generatePermutations()

	def generatePermutations(self):
		initList = [ self.init, np.fliplr(self.init), np.flipud(self.init) ]
		permutations = copy(initList)
		for i in initList:
			for k in [1,2,3]:
				permutations.append(np.rot90(i, k))
		return(permutations)



	def __repr__(self):
		outstr = "---\n{}\n\n{}\n---\n".format(self.init, self.final)
		return(outstr)



def patternToArray(pat):
	pat = pat.replace(".", "0").replace("#", "1").split("/")
	pat = list(map(list, pat))
	pn = np.array(pat)
	vint = np.vectorize(int)
	pn = vint(pn)
	return(pn)

def fileToTransformations(file):
	trans = list()
	with open(file, 'r') as fo:
		for line in fo:
			line = line.rstrip()
			trans.append(Transformation(line))
	return(trans)


def main():
	startPat = patternToArray(".#./..#/###")
	# print(startPat)

	patternFile = "day_21_input.txt"
	# patternFile = "day_21_test.txt"
	transformations = fileToTransformations(patternFile)

	art = Artwork(startPat, transformations)
	print("Iniital")
	print(art)
	for i in range(5):
		print("Iteration {}".format(i))
		art.division()
		# print(art)
		print("ON: {}".format(art.countOn()))


	art = Artwork(startPat, transformations)
	print("Iniital")
	print(art)
	for i in range(18):
		print("Iteration {}".format(i))
		startTime = time.process_time()
		art.division()
		print("Took {} sec".format(time.process_time() - startTime))
		# print(art)
		print("ON: {}".format(art.countOn()))




# x = np.array([[1,0,0],[0,1,0],[0,0,1]])
# y = np.arange(16).reshape((4,4))
# z = np.array([[1,0,0],[0,1,0],[0,0,2]])
# v = np.array([[1,0,0],[0,1,0],[0,0,1]])
# t = np.array([[1,0,0],[0,1,0],[0,0,3]])
# x = np.arange(64).reshape((8,8))
# sx = np.split(x, x.shape[0]/2)
# sx = list(map(lambda i: np.split(i, i.shape[1]/2, 1), sx))
# sx = [ item for sublist in sx for item in sublist]
# for i in sx:
# 	print(i)


if __name__ == "__main__":
	main()

