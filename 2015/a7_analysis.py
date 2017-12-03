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
aOut = myNet.simulate("a")
print("P1: Simulation of a: ", aOut)

myNet = Network(myFile)
myNet.gates['b'].input1 = aOut
aOut = myNet.simulate("a")
print("P2: Simulation of a: ", aOut)



