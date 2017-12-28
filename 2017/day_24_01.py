#!/usr/bin/env python

# USAGE: day_24_01.py
# Michael Chambers, 2017
from copy import copy

class Component:
	def __init__(self, c1, c2):
		self.c1 = c1
		self.c2 = c2

	def strength(self):
		return(self.c1 + self.c2)

	def isCompatible(self, cx):
		return(self.c1 == cx or self.c2 == cx)

	def otherEnd(self, value):
		if value == self.c1:
			return(self.c2)
		elif value == self.c2:
			return(self.c1)
		else:
			return(None)
		
	def __repr__(self):
		outstr = "{} / {}".format(self.c1, self.c2)
		return(outstr)


def componentsfromFile(file):
	comps = list()
	with open(file, 'r') as fo:
		for line in fo:
			line = line.rstrip()
			ls = line.split("/")
			comps.append(Component(int(ls[0]), int(ls[1])))
	return(comps)


def constructBridge(terminalBridge, terminalValue, compList):
	strengths = list()
	for c in compList:
		# print(c, terminalValue)
		if c.c1 == terminalValue:
			print("c1", c, terminalValue)
			newList = compList.copy()
			newList.remove(c)
			strengths.append(constructBridge(c, c.c2, newList))
		elif c.c2 == terminalValue:
			print("c2", c, terminalValue)
			newList = compList.copy()
			newList.remove(c)
			strengths.append(constructBridge(c, c.c1, newList))

	if len(strengths) == 0:
		print("Terminating bridge")
		return(terminalBridge.c1 + terminalBridge.c2)
	else:
		return(terminalBridge.c1 + terminalBridge.c2 + max(strengths))

def constructBridgeList(currentBridge, bridges, terminalValue, partList):
	extended = False
	for c in partList:
		if c.c1 == terminalValue or c.c2 == terminalValue:
			extended = True
			if c.c1 == terminalValue:
				newTerminus = c.c2
			else:
				newTerminus = c.c1

			remaining = partList.copy()
			remaining.remove(c)

			newBridge = currentBridge.copy()
			newBridge.append(c)
			# print(currentBridge, bridges, c.c2, remaining)
			# print("c1 {} {}".format(terminalValue, newBridge))
			constructBridgeList(newBridge, bridges, newTerminus, remaining)
	if not extended:
		bridgeToAdd = currentBridge.copy()
		bridges.append(bridgeToAdd)
		# print("Terminating bridge {}".format(bridgeToAdd))
	return(bridges)

def longestBridges(bridgeList):
	maxlength = 0
	for b in bridgeList:
		if len(b) > maxlength:
			maxlength = len(b)
			# print("new max: {}".format(maxlength))
	longestBridges = list()
	for b in bridgeList:
		if len(b) == maxlength:
			# print("Found longest {}".format(b))
			longestBridges.append(b)
	return(longestBridges)

def strongestBridges(bridgeList):
	maxstrength = 0
	for b in bridgeList:
		strength = sum([x.strength() for x in b])
		if strength > maxstrength:
			maxstrength = strength
	strongestBridges = list()
	for b in bridgeList:
		strength = sum([x.strength() for x in b])
		if strength == maxstrength:
			strongestBridges.append(b)
	return(strongestBridges)

def bridgeStrength(bridge):
	return(sum([x.strength() for x in bridge]))

def part1(file):
	comps = componentsfromFile(file)
	initComp = Component(0,0)
	print(constructBridge(initComp, 0, comps))

def part2(file):
	comps = componentsfromFile(file)
	initComp = Component(0,0)
	bridges = constructBridgeList(list(), list(), 0, comps)
	# for i in bridges:
		# print(i)
	# print("---")
	longest = longestBridges(bridges)
	# for i in longest:
		# print(i)
	# print("---")
	longAndStrong = strongestBridges(longest)
	for i in longAndStrong:
		print(i)
		print(bridgeStrength(i))
	print("---")


def main():
	file = "day_24_input.txt"
	# file = "day_24_test.txt"
	# part1(file)
	part2(file)




if __name__ == "__main__":
	main()

