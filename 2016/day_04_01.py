#!/usr/bin/env python

# USAGE: day_04_01.py
# Michael Chambers, 2015

from collections import defaultdict, OrderedDict

class Room(object):
	def __init__(self, line):
		ls = line.rstrip().split("-")

		self.name = ls[:-1]
		self.name = "".join(self.name)
		self.name = self.name.replace("-","")

		self.letters = defaultdict(int)
		for l in self.name:
			self.letters[l] += 1
		self.letters = OrderedDict(sorted(self.letters.items(), key= lambda t: t[0]))

		self.roomid, self.cksum = ls[-1].rstrip("]").split("[")
		
		self.roomid = int(self.roomid)


	def mostCommonLetterString(self):
		sortkeys = sorted(self.letters, key = self.letters.get, reverse=True)
		sortstr = ''.join(sortkeys)
		return(sortstr[:5])


	def isValid(self):
		if self.mostCommonLetterString() == self.cksum:
			return(True)
		else:
			return(False)

	def __str__(self):
		outstr = format("{} {} {}".format(self.name, self.roomid, self.cksum))
		return(outstr)


def main():
	file = "day_04_input.txt"
	# file = "day_04_test.txt"
	with open(file, 'r') as fo:
		valid = 0
		for line in fo:
			lroom = Room(line)
			print(lroom)
			print(lroom.mostCommonLetterString())
			if lroom.isValid():
				valid += lroom.roomid
		print("Valid sum: {}".format(valid))



if __name__ == '__main__':
	main()