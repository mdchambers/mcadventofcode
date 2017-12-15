#!/usr/bin/env python

# USAGE: day_13_01.py
# Michael Chambers, 2015

from collections import defaultdict



class Firewall:
	def __init__(self, file):
		layers = Firewall.loadFirewall(file)
		self.ranges = list()
		self.pos = list()
		# self.valuemap = list()
		for l in layers:
			while(len(self.ranges) < int(l[0])):
				self.ranges.append(0)
				self.valuemap.append([0])
			self.ranges.append(int(l[1]))
			# vmap = list(range(int(l[1]))) + list(range(int(l[1]) - 2, 0, -1))
			# self.valuemap.append(vmap)
		self.pos = [0] * len(self.ranges)
		self.sweepDown = [True] * len(self.ranges)

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

	def update(self):
		for i in range(len(self.pos)):
			# self.pos[i] += 1
			# if self.pos[i] >= len(self.valuemap[i]):
				 self.pos[i] = 0
			# if self.ranges[i] == 0:
			# 	continue
			# if self.sweepDown[i]:
			# 	self.pos[i] += 1
			# else:
			# 	self.pos[i] -= 1
			# if self.pos[i] >= self.ranges[i]:
			# 	self.sweepDown[i] = False
			# 	self.pos[i] -= 2
			# if self.pos[i] < 0:
			# 	self.sweepDown[i] = True
			# 	self.pos[i] += 2

	def reset(self):
		self.pos = [0] * len(self.ranges)
		# self.sweepDown = [True] * len(self.ranges)

	def caught(self, range):
		if self.ranges[range] > 0:
			print("Caught: {} {}".format(range, self.pos[range], self.valuemap[range][self.pos[range]]))
			return(self.valuemap[range][self.pos[range]])
		else:
			return(False)

	def traverse(self, offset):
		self.reset()
		while(offset > 0):
			self.update()
			offset -= 1
		pos = -1
		severity = 0
		caught = False
		while pos < len(self.ranges) - 1:
			pos += 1
			if self.caught(pos):
				caught = True
				severity += pos*self.ranges[pos]
			self.update()
			# print(self)
		return((caught, severity))

	def __repr__(self):
		pass

	def __str__(self):
		outstr = ""
		for i,j in enumerate(self.ranges):
			outstr += "{} : {} : {} : {}\n".format(i, j, self.pos[i], self.valuemap[i])
		return(outstr)



def main():
	# walls = Firewall("day_13_input.txt")
	walls = Firewall("day_13_test.txt")
	print(walls)
	severity = walls.traverse(0)
	print("Severity: {}".format(severity))

	# offset = 0
	# while True:
	# 	caught, severity = walls.traverse(offset)
	# 	print("Offset: {} Caught: {} Severity: {}".format(offset, caught, severity))
	# 	if not caught:
	# 		break
	# 	offset += 1









if __name__ == '__main__':
	main()