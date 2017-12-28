#!/usr/bin/env python

# USAGE: day_16_01.py
# Michael Chambers, 2017

from copy import copy

class Dance(object):
	def __init__(self, steps = None, file = None):
		if file:
			self.steps = Dance.parseSteps(file)
		else:
			self.steps = steps
		self.programs = list("abcdefghijklmnop")

	@staticmethod
	def parseSteps(file):
		dance = open(file, 'r').read().rstrip().split(",")
		steps = list()
		for raw in dance:
			s = list()
			s.append(raw[0])
			coms = raw[1:].split("/")
			if raw[0] == "s":
				coms[0] = int(coms[0])
			elif raw[0] == "x":
				coms[0] = int(coms[0])
				coms[1] = int(coms[1])
			s.append(coms)
			steps.append(s)
		return(steps)

	def doDance(self):
		for s in self.steps:
			if s[0] == "s":
				self.spin(s[1][0])
			elif s[0] == "x":
				self.exchange(s[1][0], s[1][1])
			elif s[0] == "p":
				self.partner(s[1][0], s[1][1])

	def reset(self):
		self.programs = list("abcdefghijklmnop")

	def repDance(self, number):
		cycle = self.findCycle()
		toDance = number % cycle
		self.reset()
		print("Performing {} cycles".format(toDance))
		while toDance > 0:
			self.doDance()
			toDance -= 1


	def findCycle(self):
		self.reset()
		cnum = 0
		initialState = self.programs.copy()
		while True:
			cnum += 1
			self.doDance()
			if self.programs == initialState:
				# print("Cycle: {} State: {}".format(cycleNumber, d))
				return(cnum)

	def spin(self, n):
		splitIndex = len(self.programs) - n
		self.programs = self.programs[splitIndex:] + self.programs[:splitIndex]

	def exchange(self, pos1, pos2):
		pos1Old = self.programs[pos1]
		self.programs[pos1] = self.programs[pos2]
		self.programs[pos2] = pos1Old

	def partner(self, prog1, prog2):
		prog1Index = self.programs.index(prog1)
		prog2Index = self.programs.index(prog2)
		self.exchange(prog1Index, prog2Index)

	def __repr__(self):
		outstr = ''.join(self.programs)
		return(outstr)


def part1(file):
	d = Dance(file = file)
	d.doDance()
	print(d)


def part2(file):
	#Find cycle
	d = Dance(file = file)
	d.repDance(1000000000)
	print(d)



def main():
	file = "day_16_input.txt"
	# file = "day_16_test.txt"

	part1(file)
	part2(file)









if __name__ == "__main__":
	main()

