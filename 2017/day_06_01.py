#!/usr/bin/env python

# USAGE: day_06_01.py
# Michael Chambers, 2015

myinput = "day_06_input.txt"
myinput = open(myinput, 'r').read().rstrip()
myinput = myinput.split("\t")
myinput = list(map(int, myinput))


class Banks(object):
	def __init__(self, initial_set):
		self.cbank = initial_set
		self.prevbanks = list()
		self.cycles = 0
		# print(self.cbank)

	def redistribute(self):
		self.cycles += 1
		self.prevbanks.append(list(self.cbank))

		maxCell = [i for i,x in enumerate(self.cbank) if x == max(self.cbank)][0]
		redisAmt = self.cbank[maxCell]
		self.cbank[maxCell] = 0
		currCell = maxCell
		while redisAmt > 0:
			currCell += 1
			if currCell >= len(self.cbank):
				currCell = 0
			self.cbank[currCell] += 1
			redisAmt -= 1
		# print(self.cbank)

	def checkRepeat(self):
		# print(self.cbank)
		# print(self.prevbanks)
		if self.cbank in self.prevbanks:
			return True
		else:
			return False

banks = Banks(myinput)
while(not banks.checkRepeat()):
	# if banks.cycles % 100 == 0:
	# 	print("Cycle: ", banks.cycles)
	banks.redistribute()

print("Exiting after {} cycles".format(banks.cycles))

## Part 2

cycleStart = [i for i,x in enumerate(banks.prevbanks) if x == banks.cbank]
# print("Found loop starting in cycle ", cycleStart + 1)
print("Cycles in loop: ", len(banks.prevbanks) - cycleStart[0])