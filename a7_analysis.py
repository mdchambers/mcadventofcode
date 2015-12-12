#!/usr/bin/env python

# USAGE: a7_analysis.py
# Michael Chambers, 2015
from __future__ import print_function
import sys


def log(*msg):
	print("LOG: ", *msg, file = sys.stderr)

class Gate(object):
	def __init__(self, line):
		ll = line.split()
		# Gate is an identity gate ( x -> y)
		if len(ll) == 3:
			self.input1 = ll[0]
			self.type = "IDENTITY"
			self.output = ll[2]
		# Gate is a NOT gate
		if len(ll) == 4:
			self.type = "NOT"
			self.input1 = ll[1]
			self.input2 = None
			self.output = ll[3]
		# Gate is something else and/or/lshift/rshift/
		elif len(ll) == 5:
			self.input1 = ll[0]
			self.type = ll[1]
			self.input2 = ll[2]
			self.output = ll[4]
		self.outputValue = None


class Network(object):
	def __init__(self, netFName):
		self.gates = dict()
		netFile = open(netFName, 'r')
		while True:
			line = netFile.readline().rstrip()
			if not line: break
			currGate = Gate(line)
			self.gates[currGate.output] = currGate

	def simulate(self, desOutput):
		log("simulate called with key ", desOutput)
		try:
			output = int(desOutput)
			return(output)
		except ValueError:
			pass
		desGate = self.gates[desOutput]
		if desGate.outputValue: return(desGate.outputValue)
		if desGate.type == "IDENTITY":
			try:
				output = int(desGate.input1)
				return(output)
			except ValueError:
				desGate.outputValue = self.simulate(desGate.input1)
				return(desGate.outputValue)
		elif desGate.type == "NOT":
			desGate.outputValue = ~ self.simulate(desGate.input1)
			return(desGate.outputValue)
		elif desGate.type == "AND":
			desGate.outputValue = self.simulate(desGate.input1) & self.simulate(desGate.input2)
			return(desGate.outputValue)
		elif desGate.type == "OR":
			desGate.outputValue = self.simulate(desGate.input1) | self.simulate(desGate.input2)
			return(desGate.outputValue)
		elif desGate.type == "RSHIFT":
			desGate.outputValue = self.simulate(desGate.input1) >> int(desGate.input2)
			return(desGate.outputValue)
		elif desGate.type == "LSHIFT":
			desGate.outputValue = self.simulate(desGate.input1) << int(desGate.input2)
			return(desGate.outputValue)
		else:
			log("Error could not find gate producing ", desOutput)

myFile = "a7_input.txt"
myNet = Network(myFile)
print("Simulation of a: ", myNet.simulate("a"))
# def calcValue(output):
# 	mfile = "a7_input.txt"
# 	while True:
# 		# Read a line
# 		line = mfile.readline().rstrip()
# 		# If cannot read line, something has gone wrong
# 		if not line:
# 			print("Error could not find gate producing ", output, file = sys.stderr)
# 			break
# 		# Parse line into gate object
# 		gate = Gate(line)
# 		# Check if current gate generates the desired output
# 		if gate.output == output:
# 			# Check if single input gate, meaning either NOT, identity, or input gate
# 			if gate.input2 is None:
# 				try:
# 					# Gate is input
# 					return(int(gate.input1))
# 				except ValueError:
# 					# Gate is NOT, return NOT'd value
# 					myInput1 = calcValue(gate.input1))
# 					return( ~ myInput1)
# 			else:
# 				# Calculate inputs
# 				myInput1 = calcValue(gate.input1)
# 				myInput2 = calcValue(gate.input2)

# 		else:
# 			continue


# calcValue("a")

# mfile = "a7_input.txt"
# gates = list()
# while True:
# 	line = mfile.readline().rstrip()
# 	ll = line.split()
# 	if len(ll) == 4:

# 	gates.append(line)