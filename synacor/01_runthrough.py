#!/usr/bin/env python

# USAGE: solution_01.py
# Michael Chambers, 2017

import sys
# from collections import defaultdict
from Architecture import Architecture

def main():
	debug = False
	if len(sys.argv) > 1:
		debug = True
	file = "challenge.bin"
	arch = Architecture(file)
	# for i in arch.commands:
		# print(i)
	# arch.run()
	# arch.registers[7] = 1
	arch.run(debug = debug)



if __name__ == "__main__":
	main()








