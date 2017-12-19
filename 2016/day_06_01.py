#!/usr/bin/env python

# USAGE: day_06_01.py
# Michael Chambers, 2015

from collections import defaultdict

def main():
	file = "day_06_input.txt"
	with open(file, 'r') as fo:
		positions = list()
		for line in fo:
			line = line.rstrip()
			for i, p in enumerate(line):
				if i >= len(positions):
					positions.append(defaultdict(int))
				positions[i][p] += 1

		output = ""
		for dd in positions:
			maxkey = max(dd.keys(), key = lambda x: dd[x])
			output += maxkey
		print("Error corrected: {}".format(output))

	with open(file, 'r') as fo:
		positions = list()
		for line in fo:
			line = line.rstrip()
			for i, p in enumerate(line):
				if i >= len(positions):
					positions.append(defaultdict(int))
				positions[i][p] += 1

		output = ""
		for dd in positions:
			maxkey = min(dd.keys(), key = lambda x: dd[x])
			output += maxkey
		print("Error corrected: {}".format(output))




if __name__ == '__main__':
	main()