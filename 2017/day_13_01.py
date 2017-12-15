#!/usr/bin/env python

# USAGE: day_13_01.py
# Michael Chambers, 2015

from collections import defaultdict



class Firewall:
	def __init__(self, file):
		layers = Firewall.loadFirewall(file)
		self.time = 0
		self.ranges = list()
		self.pos = list()
		self.valuemap = list()
		for l in layers:
			while(len(self.ranges) < int(l[0])):
				self.ranges.append(0)
				self.valuemap.append([0])
			self.ranges.append(int(l[1]))
			vmap = list(range(int(l[1]))) + list(range(int(l[1]) - 2, 0, -1))
			self.valuemap.append(vmap)
		self.pos = [0] * len(self.ranges)
		# self.sweepDown = [True] * len(self.ranges)

	# Loads firewall data from file
	# Returns 
	@staticmethod
	def loadFirewall(file):
		fh = open(file, 'r')
		firewalls = list()
		for line in fh:
			line = line.rstrip().replace(":", "")
			ls = line.split(" ")
			firewalls.append(tuple(ls))
		fh.close()
		return(firewalls)

	def setOffset(self, time):
		self.time = time
		for i in range(len(self.pos)):
			vmappos = self.time % (2 * self.ranges[i] -2)
			self.pos[i] = self.valuemap[i][vmappos]

	def increment(self):
		self.setOffset(self.time + 1)

	def reset(self):
		self.setOffset(0)

	def caught(self, ran):
		if self.ranges[ran] > 0:
			if self.valuemap[ran][self.pos[ran]] == 0:
				return(True)
		else:
			return(False)

	def traverse(self, offset):
		self.setOffset(offset)
		pos = 0
		severity = 0
		caught = False
		while pos < len(self.ranges):
			if self.caught(pos):
				caught = True
				severity += pos*self.ranges[pos]
			self.increment()
			pos += 1

		return((caught, severity))

	def checkIfClearable(self, time):
		for n, r in enumerate(self.ranges):
			if r == 0:
				continue
			cpos = (time + n) % (2 * r - 2)
			if cpos == 0:
				return(False)
		return(True)

	def __repr__(self):
		pass

	def __str__(self):
		outstr = ""
		for i,j in enumerate(self.ranges):
			outstr += "{} : {} : {} : {}\n".format(i, j, self.pos[i], self.valuemap[i])
		return(outstr)



def main():
	walls = Firewall("day_13_input.txt")
	# walls = Firewall("day_13_test.txt")
	caught, severity = walls.traverse(0)
	print("Severity: {}".format(severity))

	offset = 0
	while True:
		print("Checking offset: {}".format(offset))
		if walls.checkIfClearable(offset):
			break
		offset += 1
	print("Clearable offset: {}".format(offset))

if __name__ == '__main__':
	main()