#!/usr/bin/env python

# USAGE: day_23_01.py
# Michael Chambers, 2017

import atexit
import sys
import re
from collections import defaultdict

class InstructionList():
	def __init__(self, file):
		self.instructions = list()
		self.registers = defaultdict(int)
		self.currentProg = 0
		with open(file, 'r') as fo:
			for line in fo:
				line = line.rstrip()
				ls = line.split(" ")
				self.instructions.append(ls)

	def run(self, watch = False):
		try:
			commandSums = defaultdict(int)
			watchval = 0
			currentstep = 0
			while True:
				currentstep += 1
				# if watch and currentstep % 100000 == 0:
				if watch:
					# print(self.currentProg)
					# print("{} {}".format(currentstep, self.registers))
					print(self.registers)
				# print(currentProg)
				command = self.instructions[self.currentProg][0]
				arg1 = self.instructions[self.currentProg][1]
				arg2 = self.instructions[self.currentProg][2]
				
				try:
					arg2Val = int(arg2)
				except ValueError as ex:
					arg2Val = int(self.registers[arg2])

				commandSums[command] += 1

				if command == "set":
					self.registers[arg1] = arg2Val
				elif command == "sub":
					self.registers[arg1] -= arg2Val
				elif command == "mul":
					self.registers[arg1] *= arg2Val

				try:
					arg1Val = int(arg1)
				except ValueError as ex:
					arg1Val = self.registers[arg1]
				if command == "jnz" and arg1Val != 0:
					self.currentProg = self.currentProg + arg2Val
					if self.currentProg < 0 or self.currentProg >= len(self.instructions):
						print("BREAKING")
						break
				else:
					self.currentProg += 1
			return(commandSums)
		except KeyboardInterrupt as ex:
			sys.exit()
		finally:
			print("Resume data:\nPos\n{}\nValues\n{}".format(self.currentProg, self.registers))




# def goodbye(obj):
	# print("Resume data: Pos\n{}\nValues\n{}".format(obj.currentProg, obj.registers))


def part1(file):
	il = InstructionList(file)
	comsum = il.run()
	print("Part1: {}".format(comsum["mul"]))

def part2(file):
	h = 0
	b = 109900
	c = 126900
	while True:
		f = 1
		d = 2	
		while True:
			if b % d == 0:
				f = 0
			d += 1	
			if d == b:
				break
		if f == 0:
			h += 1
		if c == b:
			break
		b += 17
		print(h)
	print(h)



def main():
	# file = "day_23_input.txt"
	file = "day_23_test.txt"
	# part1(file)
	part2(file)





if __name__ == "__main__":
	main()

