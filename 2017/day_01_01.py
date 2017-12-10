#!/usr/bin/env python

# USAGE: day_01_01.py
# Michael Chambers, 2015

import itertools

file = "day_01_input.txt"
nums = open(file, 'r').read().rstrip()
numlist = list(map(int, list(nums)))

# Part 1

total = 0

for a in zip(numlist[1:], numlist[:-1]):
	# print(a)
	if a[0] == a[1]:
		total += a[0]

if numlist[0] == numlist[-1]:
	total += numlist[-1]

print(total)

# Part 2

total = 0

numlist2 = itertools.chain(numlist[int(len(numlist)/2):], numlist[:int(len(numlist))])

for a in zip(numlist, numlist2):
	# print(a)
	if a[0] == a[1]:
		total += a[0]

print(total)