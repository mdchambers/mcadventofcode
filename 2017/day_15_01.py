#!/usr/bin/env python

# USAGE: day_15_01.py
# Michael Chambers, 2015


## Puzzle input
initialA = 512
initialB = 191

## Test data
# initialA = 65
# initialB = 8921


def generate(inA, inB):
	outA = (16807 * inA ) % 2147483647
	outB = (48271 * inB ) % 2147483647
	return(outA, outB)

def compare(inA, inB):
	binA = bin(inA)[-16:]
	binB = bin(inB)[-16:]
	if binA == binB:
		return True
	return False

def generateWithConstraint(inA, inB):
	outA = (16807 * inA ) % 2147483647
	while outA % 4 != 0:
		outA = (16807 * outA ) % 2147483647
	outB = (48271 * inB ) % 2147483647
	while outB % 8 != 0:
		outB = (48271 * outB ) % 2147483647
	return(outA, outB)

def main():

	## Part 1
	currentA = initialA
	currentB = initialB

	count = 0
	for x in range(40000000):
		newA, newB = generate(currentA, currentB)
		if compare(newA, newB):
			count += 1
		currentA = newA
		currentB = newB
		if x % 100000 == 0:
			print(x)
	print("Matched: {}".format(count))

	### Part 2
	currentA = initialA
	currentB = initialB

	count = 0
	for x in range(5000000):
		newA, newB = generateWithConstraint(currentA, currentB)
		if compare(newA, newB):
			count += 1
		currentA = newA
		currentB = newB
		if x % 100000 == 0:
			print(x)
	print("Matched: {}".format(count))




if __name__ == '__main__':
	main()

