#!/usr/bin/env python

# USAGE: day_16_01.py
# Michael Chambers, 2017

class DanceGroup(object):
	def __init__(self):
		self.programs = list("abcdefghijklmnop")

		# For testing
		# self.programs = list("abcde")

	def __str__(self):
		return(''.join(self.programs))

	def resetOrder(self):
		self.programs = list("abcdefghijklmnop")

	def applyDance(self, dance):
		self.programs


class Dance(object):
	def __init__(self, steps = None, file = None, length = 16):
		if file:
			self.steps = Dance.parseSteps(file)
		else:
			self.steps = steps
		self.mapping = self.getMapping()
		self.length = length

	@staticmethod
	def parseSteps(file):
		dance = open(file, 'r').read().rstrip().split(",")
		steps = list()
		for raw in dance:
			s = list()
			s.append(raw[0])
			coms = raw[1:].split("/")
			s.append(coms)
			steps.append(s)
		return(steps)

	@staticmethod
	def fromRep(dance, n):
		newDance = Dance()
		return(newDance)

	def getMapping(self):
		mapvec = list(range(self.length))
		for s in self.steps:
			if s[0] == "s":
				self.spin(s[1][0])
			elif s[0] == "x":
				self.exchange(s[1][0], s[1][1])
			elif s[0] == "p":
				self.partner(s[1][0], s[1][1])

	def spin(self, n):
		n = int(n)
		splitIndex = len(self.programs) - n
		self.programs = self.programs[splitIndex:] + self.programs[:splitIndex]

	def exchange(self, pos1, pos2):
		pos1, pos2 = (int(pos1), int(pos2))
		pos1Old = self.programs[pos1]
		self.programs[pos1] = self.programs[pos2]
		self.programs[pos2] = pos1Old

	def partner(self, prog1, prog2):
		prog1Index = self.programs.index(prog1)
		prog2Index = self.programs.index(prog2)
		self.exchange(prog1Index, prog2Index)
		

def main():
	file = "day_16_input.txt"
	# file = "day_16_test.txt"

	group = DanceGroup()
	dance = Dance(file = file)
	group.doDance(dance)
	print("Part 1: {}".format(group))

	# group2 = DanceGroup()
	# # for i in range(1000000000):
	# for i in range(1000):
	# 	group2.doDance(steps)
	# 	if i % 10000 == 0:
	# 		print(i)
	# print("Part 2: {}".format(group2))





if __name__ == "__main__":
	main()

