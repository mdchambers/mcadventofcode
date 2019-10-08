#!/usr/bin/env python

# USAGE: temp.py
# Michael Chambers, 2017

# from sys import stdin
import sys
import itertools

def func(vals):
	return(vals[0] + vals[1] * vals[2] ** 2 + vals[3] ** 3 - vals[4])

def main():
	x = [2,3,5,7,9]
	for i in itertools.permutations(x):
		# print(func(i))
		if func(i) == 399:
			print(i)

if __name__ == "__main__":
	main()

