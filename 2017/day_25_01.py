#!/usr/bin/env python

# USAGE: day_25_01.py
# Michael Chambers, 2017

import sys
import re
from collections import defaultdict


class State(object):
	def __init__(self, write, move, cont):
		self.write = tuple(map(int, write))
		def parseWrite(i):
			if i == "right":
				return(1)
			else:
				return(-1)
		self.move = tuple(map(parseWrite, move))
		self.cont = cont

	def __repr__(self):
		outstr = "Write: {} Move: {} Cont: {}\n".format(self.write, self.move, self.cont)
		return(outstr)



def parseBlueprints(file):
	with open(file, 'r') as fo:
		startState = ""
		diagnostic = 0
		cdata = list()
		states = dict()
		for line in fo:
			line = line.rstrip()
			# if re.search(r"Begin", line):
			# 	m = re.search(r" (.)\.", line)
			# 	startState = m.group(1)
			# 	continue
			# if re.search(r"Perform", line):
			# 	m = re.search(r" (.)+ steps", line)
			# 	diagnostic = int(m.group(1))
			# 	continue
			if re.search("In state", line):
				# print(cdata)
				if len(cdata) > 0:
					states[cdata[0]] = State( ( cdata[1], cdata[4]), (cdata[2], cdata[5]), (cdata[3], cdata[6]))
				cdata = list()
				m = re.search(r"(.):", line)
				cdata.append(m.group(1))
			if re.search("Write", line):
				m = re.search("value (.)", line)
				cdata.append(m.group(1))
			if re.search("Move", line):
				m = re.search(r"to the (.+)\.", line)
				cdata.append(m.group(1))
			if re.search("Continue", line):
				m = re.search("state (.)", line)
				cdata.append(m.group(1))
		states[cdata[0]] = State( ( cdata[1], cdata[4]), (cdata[2], cdata[5]), (cdata[3], cdata[6]))
		return(states)

def parseStartState(file):
	with open(file, 'r') as fo:
		startState = ""
		for line in fo:
			line = line.rstrip()
			if re.search(r"Begin", line):
				m = re.search(r" (.)\.", line)
				startState = m.group(1)
				break
		return(startState)

def parseDiagnostic(file):
	with open(file, 'r') as fo:
		diagnostic = 0
		for line in fo:
			line = line.rstrip()
			if re.search(r"Perform", line):
				m = re.search(r"after (.+) steps", line)
				diagnostic = int(m.group(1))
				break
		return(diagnostic)


def runMachine(states, initialState, cycles):
	currState = initialState
	currCycle = 1

	pos = 0
	registers = defaultdict(int)
	while currCycle <= cycles:
		regState = registers[pos]
		registers[pos] = states[currState].write[regState]

		pos = pos + states[currState].move[regState]

		currState = states[currState].cont[regState]

		currCycle += 1
		if currCycle % 1000000 == 0:
			print("Cycle: {}".format(currCycle))
	return(registers)




def main():
	file = "day_25_input.txt"
	states = parseBlueprints(file)

	startState = parseStartState(file)
	endCycle = parseDiagnostic(file)
	# endCycle = 10
	reg = runMachine(states, startState, endCycle)
	# print(reg)

	checksum = sum(reg.values())
	print("Checksum: {}".format(checksum))



if __name__ == "__main__":
	main()

