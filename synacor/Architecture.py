#!/usr/bin/env python

# USAGE: solution_01.py
# Michael Chambers, 2017

import sys
# from collections import defaultdict

class Architecture:
	def __init__(self, file):
		self.pos = 0
		self.registers = [0] * 8
		self.stack = list()
		self.functions = self.generateFunctions()
		self.commands = self.loadCommands(file)
		# self.memory = defaultdict(int)
		self.minput = ""

	def getValue(self, pos):
		if self.commands[pos] <= 32767:
			return(self.commands[pos])
		elif self.commands[pos] <= 32775:
			return(self.registers[self.commands[pos] - 32768])
		else:
			print("INVALID VALUE")
			return(None)

	def setRegister(self, reg, val):
		# print("setting reg {} to val {}".format(reg, val))
		if reg > 7:
			reg = reg - 32768
		self.registers[reg] = val

	def getRegister(self, reg):
		if reg > 7:
			reg = reg - 32768
		return(self.registers[reg])

	def fhalt(self, identify = False):
		if identify:
			print("terminating at position: {}".format(self.pos))
			print("set: {}".format(self.registers))
		self.terminate = True

	# set: 1 a b
	# Set register <a> to the value of <b>
	def fset(self, identify = False):
		# print("before set: {}".format(self.registers))
		if identify:
			print("set called: pos {} register {} from {} to  {}".format(self.pos, self.commands[self.pos + 1] - 32768, self.getValue(self.pos + 1), self.getValue(self.pos + 2)))
		self.setRegister(self.commands[self.pos + 1], self.getValue(self.pos + 2))
		# print("after set: {}".format(self.registers))
		self.pos += 3

	# push: 2 a
  	# push <a> onto the stack
	def fpush(self, identify = False):
		if identify:
			print("push called")
		self.stack.append(self.getValue(self.pos + 1))
		self.pos += 2

	# pop: 3 a
 	# remove the top element from the stack and write it into <a>; empty stack = error
	def fpop(self, identify = False):
		if identify:
			print("pop called")
		self.setRegister(self.commands[self.pos + 1], self.stack.pop())
		self.pos += 2
	# eq: 4 a b c
	# set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
	def feq(self, identify = False):
		if self.getValue(self.pos + 2) == self.getValue(self.pos + 3):
			self.setRegister(self.commands[self.pos + 1], 1)
		else:
			self.setRegister(self.commands[self.pos + 1], 0)
		if identify:
			print("eq called: pos {} a {} b {} result {}".format(self.pos, self.getValue(self.pos + 2), self.getValue(self.pos + 3), self.getValue(self.pos + 2) == self.getValue(self.pos + 3)))
		self.pos += 4

	# gt: 5 a b c
 	# set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
	def fgt(self, identify = False):
		if identify:
			print("gt called")
		if self.getValue(self.pos + 2) > self.getValue(self.pos + 3):
			self.setRegister(self.commands[self.pos + 1], 1)
		else:
			self.setRegister(self.commands[self.pos + 1], 0)
		self.pos += 4


	def fjmp(self, identify = False):
		if identify:
			print("jmp called: pos: {} to position: {}".format(self.pos, self.commands[self.pos + 1]))
		self.pos = self.commands[self.pos + 1]

	# If <a> is nonzero, jump to <b>
	def fjt(self, identify = False):
		if identify:
			print("jt called: pos: {} on value: {} to: {}".format(self.pos, self.getValue(self.pos + 1), self.commands[self.pos + 2]))
		if self.getValue(self.pos + 1) != 0:
			self.pos = self.commands[self.pos + 2]
		else:
			self.pos = self.pos + 3

	# If <a> is zero, jump to <b>
	def fjf(self, identify = False):
		if identify:
			print("jf called: pos: {} on value: {} to: {}".format(self.pos, self.getValue(self.pos + 1), self.commands[self.pos + 2]))
		if self.getValue(self.pos + 1) == 0:
			self.pos = self.commands[self.pos + 2]
		else:
			self.pos = self.pos + 3

	# add: 9 a b c
	# assign into <a> the sum of <b> and <c> (modulo 32768)
	def fadd(self, identify = False):
		newval = self.getValue(self.pos + 2) + self.getValue(self.pos + 3)
		newval = newval % 32768
		if identify:
			print("add called: pos: {} reg: {} + {} = {}".format(self.pos, self.commands[self.pos + 1] - 32768, self.getValue(self.pos + 2), self.getValue(self.pos + 3), newval))
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 4

	# mult: 10 a b c
	# store into <a> the product of <b> and <c> (modulo 32768)
	def fmult(self, identify = False):
		if identify:
			print("mult called")
		newval = self.getValue(self.pos + 2) * self.getValue(self.pos + 3)
		newval = newval % 32768
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 4

	# mod: 11 a b c
 	# store into <a> the remainder of <b> divided by <c>
	def fmod(self, identify = False):
		if identify:
			print("mod called")
		newval = self.getValue(self.pos + 2) % self.getValue(self.pos + 3)
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 4

	# and: 12 a b c
  	# stores into <a> the bitwise and of <b> and <c>
	def fand(self, identify = False):
		if identify:
			print("and called")
		newval = self.getValue(self.pos + 2) & self.getValue(self.pos + 3)
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 4

	# or: 13 a b c
  	# stores into <a> the bitwise or of <b> and <c>	
	def ffor(self, identify = False):
		if identify:
			print("or called")
		newval = self.getValue(self.pos + 2) | self.getValue(self.pos + 3)
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 4

	# not: 14 a b
	# stores 15-bit bitwise inverse of <b> in <a>
	def fnot(self, identify = False):
		if identify:
			print("not called")
		newval = 0b111111111111111 ^ self.getValue(self.pos + 2)
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 3

	# rmem: 15 a b
	# read memory at address <b> and write it to <a>
	def frmem(self, identify = False):
		if identify:
			print("rmem called: pos: {} from: {} to: {}".format(self.pos, self.getValue(self.pos + 2), self.commands[self.pos + 1]))
		newval = self.commands[self.getValue(self.pos + 2)]
		self.setRegister(self.commands[self.pos + 1], newval)
		self.pos += 3

	# wmem: 16 a b
 	# write the value from <b> into memory at address <a>
	def fwmem(self, identify = False):
		if identify:
			print("wmem called: pos: {} from: {} to address: {}".format(self.pos, self.getValue(self.pos + 2), self.getValue(self.pos + 1)))
		newval = self.getValue(self.pos + 2)
		self.commands[self.getValue(self.pos + 1)] = newval
		self.pos += 3

	# call: 17 a
  	# write the address of the next instruction to the stack and jump to <a>
	def fcall(self, identify = False):
		if identify:
			print("call called: pos: {} stack: {} jump to: {}".format(self.pos, self.pos + 2, self.getValue(self.pos + 1)))
		self.stack.append(self.pos + 2)
		self.pos = self.getValue(self.pos + 1)

	# ret: 18
	# remove the top element from the stack and jump to it; empty stack = halt
	def fret(self, identify = False):
		if identify:
			print("ret called")
		if len(self.stack) == 0:
			self.fhalt()
		else:
			self.pos = self.stack.pop()

	def fout(self, identify = False):
		if identify:
			print("out called")
		# print("printing char {} as {}".format())
		print(chr(self.getValue(self.pos + 1)), end = '')
		self.pos += 2

	# in: 20 a
	# read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard and trust that they will be fully read
	def fin(self, identify = False):
		if len(self.minput) > 0:
			if self.minput == "pos\n":
				print(self.pos)
				print(self.registers)
				print(len(self.stack))
			elif self.minput == "set\n":
				self.registers[7] = 1
				self.minput = sys.stdin.readline()
			elif self.minput == "pickle\n":
				pass
			else:
				self.setRegister(self.commands[self.pos + 1], ord(self.minput[0]))
				self.minput = self.minput[1:]
				self.pos += 2
		else:
			self.minput = sys.stdin.readline()
			self.fin()
		if identify:
			print("in called: pos {} writing {} to register {}".format(self.pos, ord(minput[0]), self.commands[self.pos + 1] - 32768))


	def fnoop(self, identify = False):
		if identify:
			print("noop called")
		self.pos += 1

	def generateFunctions(self):
		return((
			self.fhalt, 
			self.fset, 
			self.fpush, 
			self.fpop, 
			self.feq, 
			self.fgt, 
			self.fjmp, 
			self.fjt, 
			self.fjf, 
			self.fadd, 
			self.fmult, 
			self.fmod, 
			self.fand, 
			self.ffor, 
			self.fnot, 
			self.frmem, 
			self.fwmem, 
			self.fcall, 
			self.fret, 
			self.fout, 
			self.fin, 
			self.fnoop))

	def loadCommands(self, file):
		coms = list()
		with open(file, 'rb') as fo:
			bp = fo.read(2)
			while bp != b"":
				# print(bp)
				# coms.append(struct.unpack("<H", bp))
				coms.append(int.from_bytes(bp, byteorder = 'little'))
				bp = fo.read(2)
		return(coms)

	def run(self, debug = False):
		self.pos = 0
		self.terminate = False
		while not self.terminate:
			currval = self.commands[self.pos]
			self.functions[currval](identify = debug)
			# if debug:
				# print("set: {}".format(self.registers))

	# Dumps a human-readable version of the in-memory command list to the designated file
	# This is a bad implementation, as not all outputs are actual commands (i.e. it may misinterpret values < 21 as commands when they are never used as such)
	def outputCommands(self, file):
		coms = ("halt", "set", "push", "pop", "eq", "gt", "jmp", "jt", "jf", "add", "mult", "mod", "and", "or", "not", "rmem", "wmem", "call", "ret", "out", "in", "noop")
		jumps = (1,3,2,2,4,4,2,3,3,4,4,4,4,4,3,3,3,2,1,2,2,1)
		pos = 0
		with open(file, 'w') as fo:
			while pos < len(self.commands):
				# print(pos, self.commands[pos])
				if self.commands[pos] >= len(jumps):
					pos += 1
					continue
				endpos = pos + jumps[self.commands[pos]]
				c = self.commands[pos:endpos]
				c[0] = coms[self.commands[pos]]
				outstr = "\t".join(str(i) for i in c)
				fo.write(outstr + "\n")
				pos += jumps[self.commands[pos]]

# def main():
# 	debug = False
# 	if len(sys.argv) > 1:
# 		debug = True
# 	file = "challenge.bin"
# 	arch = Architecture(file)
# 	# for i in arch.commands:
# 		# print(i)
# 	# arch.run()
# 	# arch.registers[7] = 1
# 	arch.run(debug = debug)



# if __name__ == "__main__":
# 	main()








