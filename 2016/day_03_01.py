#!/usr/bin/env python

# USAGE: day_03_01.py
# Michael Chambers, 2015


import re
from itertools import islice, zip_longest

def checkIfValid(lens):
	if lens[0] + lens[1] > lens[2] and lens[1] + lens[2] > lens[0] and lens[0] + lens[2] > lens[1]:
		return(1)
	return(0)

def processLine(line):
	line = line.strip()
	ls = re.split(" +", line)
	ls = list(map(int, ls))	
	return(ls)

def rowsToCols(m):
	cols = list()
	for i in range(len(m)):
		cols.append([row[i] for row in m])
	return(cols)


def main():
	file = "day_03_input.txt"
	fo = open(file, 'r')

	validCount = 0
	for line in fo:
		ls = processLine(line)
		validCount += checkIfValid(ls)
	print("Total valid: {}".format(validCount))

	fo.close()
	validCount = 0
	fo = open(file, 'r')
	for lines in zip_longest(*[fo] * 3):
		rows = list(map(processLine, lines))
		cols = rowsToCols(rows)
		for c in cols:
			validCount += checkIfValid(c)
	print("Total valid: {}".format(validCount))
		


if __name__ == '__main__':
	main()