#!/usr/bin/env python

# USAGE: day_18_01.py
# Michael Chambers, 2017
from collections import defaultdict

class InstructionList:
	def __init__(self, file = None, commandList = None):
		self.instructions = list()
		if file:
			self.initFromFile(file)
		elif commandList:
			self.instructions = commandList
		self.pos = 0
		self.lastsound = 0

	def initFromFile(self, file):
		with open(file, 'r') as fo:
			for line in fo:
				line = line.rstrip()
				ls = line.split(' ')
				self.instructions.append(ls)

	def __str__(self):
		outstr = "Pos {}\nCmd {}".format(self.pos, self.instructions)
		return(outstr)

	def applyInstruction(self, registers):
		currinst = self.instructions[self.pos]

		changeVal = 0
		if len(currinst) == 3:
			try:
				changeVal = int(currinst[2])
			except ValueError as ex:
				changeVal = registers[currinst[2]]

		# print("{} {} {}".format(registers, currinst, changeVal))
		if currinst[0] == "set":
			registers[currinst[1]]  = changeVal
		elif currinst[0] == "add":
			registers[currinst[1]] += changeVal
		elif currinst[0] == "mul":
			registers[currinst[1]] *= changeVal
		elif currinst[0] == "mod":
			registers[currinst[1]] %= changeVal
		elif currinst[0] == "snd":
			self.lastsound = registers[currinst[1]]
		elif currinst[0] == "rcv":
			# print("In rcv: {} {}".format(currinst[1], registers[currinst[1]]))
			if registers[currinst[1]] != 0:
				return(self.lastsound)
		if currinst[0] == "jgz" and registers[currinst[1]] > 0:
			self.pos += changeVal
		else:
			self.pos += 1

class Program:
	def __init__(self, progNumber, file = None, commandList = None):
		self.instructions = list()
		if file:
			self.initFromFile(file)
		elif commandList:
			self.instructions = commandList
		self.pos = 0
		self.lastsound = 0
		self.registers = defaultdict(int)
		self.registers["p"] = progNumber
		
		self.outputbuffer = list()
		self.sentvals = 0
		self.locked = False

	def initFromFile(self, file):
		with open(file, 'r') as fo:
			for line in fo:
				line = line.rstrip()
				ls = line.split(' ')
				self.instructions.append(ls)

	def __str__(self):
		outstr = "Pos {}\nCmd {}".format(self.pos, self.instructions)
		return(outstr)

	def applyInstruction(self, name, partner):
		# If waiting for value and nothing in buffer, do nothing
		if self.locked and len(partner.outputbuffer) == 0:
			# print("Prog {} waiting".format(name))
			return()

		currinst = self.instructions[self.pos]

		changeVal = 0
		if len(currinst) == 3:
			try:
				changeVal = int(currinst[2])
			except ValueError as ex:
				changeVal = self.registers[currinst[2]]

		# print("{} {} {} {}".format(name, self.registers, currinst, changeVal))
		if currinst[0] == "set":
			self.registers[currinst[1]]  = changeVal
		elif currinst[0] == "add":
			self.registers[currinst[1]] += changeVal
		elif currinst[0] == "mul":
			self.registers[currinst[1]] *= changeVal
		elif currinst[0] == "mod":
			self.registers[currinst[1]] %= changeVal
		elif currinst[0] == "snd":
			try:
				sendval = int(currinst[1])
			except ValueError as ex:
				sendval = self.registers[currinst[1]]
			self.outputbuffer.append(sendval)
			self.sentvals += 1
		elif currinst[0] == "rcv":
			if len(partner.outputbuffer) > 0:
				if self.locked:
					# print("Prog {} no longer waiting".format(name))
					self.locked = False
				self.registers[currinst[1]] = partner.outputbuffer.pop(0)
			else:
				# Move backwards one step so that the final if returns us to this position, waiting for a input
				# print("Prog {} waiting".format(name))
				self.pos -= 1
				self.locked = True
		if currinst[0] == "jgz":
			try:
				testval = int(currinst[1])
			except ValueError as ex:
				testval = self.registers[currinst[1]]
			if testval > 0:
				self.pos += changeVal
			else:
				self.pos += 1
		else:
			self.pos += 1


def countSentValues(prog1, prog2):
	while not prog1.locked or not prog2.locked:
		prog1.applyInstruction("p0", prog2)
		prog2.applyInstruction("p1", prog1)
		print("Prog1: {} Prog2: {}".format(prog1.sentvals, prog2.sentvals))
		# print("Prog1: {} Prog2: {}".format(prog1.outputbuffer, prog2.outputbuffer))
		# print("Prog1: {} {} Prog2: {} {}".format(prog1.locked, len(prog1.outputbuffer), prog2.locked, len(prog2.outputbuffer)))


def main():
	mfile = "day_18_input.txt"
	# mfile = "day_18_test.txt"
	il = InstructionList(file = mfile)
	# print(il)
	registers = defaultdict(int)
	while True:
		rcv = il.applyInstruction(registers)
		if rcv:
			break
	print("Recovered sound: {}".format(rcv))

	# mfile = "day_18_test2.txt"
	prog1 = Program(0, file = mfile)
	prog2 = Program(1, file = mfile)
	countSentValues(prog1, prog2)



if __name__ == "__main__":
	main()

