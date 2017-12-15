#!/usr/bin/env python

# USAGE: day_12_01.py
# Michael Chambers, 2015

# class Prog:
# 	def __init__(self):
# 		pass
import sys

def readProgs(file):
	fh = open(file, 'r')
	progs = dict()
	for line in fh:
		line = line.rstrip().replace(",", "")
		ls = line.split(" ")
		progName = ls[0]
		progPipes = ls[2:]
		progs[progName] = progPipes
	return(progs)

# Recursively counts unique 
def countInGroup(prog, groups, groupID):
	for g in prog[groupID]:
		if g != groupID and g not in groups:
			groups.update([g])
			groups.update(countInGroup(prog, groups, g))
		if g == groupID:
			groups.update([g])
	return(groups)

def main():
	progs = readProgs("day_12_input.txt")

	inGroup = countInGroup(progs, set(), "0")

	print("Prog group with 0: {}".format(len(inGroup)))

	# Get a list of all groups as sets
	groupsets = list()
	for k in progs.keys():
		groupsets.append(countInGroup(progs, set(), k))
	print("Total groups: {}".format(len(groupsets)))

	# Create a set of sorted tuples, i.e. every element will be unique
	uniquesets = set(tuple(sorted(x)) for x in groupsets)
	print("Unique groups {}".format(len(uniquesets)))



if __name__ == "__main__":
	main()









