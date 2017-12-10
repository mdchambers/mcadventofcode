#!/usr/bin/env python

# USAGE: day_02_01.py
# Michael Chambers, 2015

import itertools

file = "day_02_input.txt"
fh = open(file, 'r')


## Part I

checksum = 0

for line in fh:
	# print("foo:", line)
	vals = line.split('\t')
	vals = list(map(int, vals))
	vmax = max(vals)
	vmin = min(vals)
	checksum += vmax - vmin

print(checksum)

fh.close()

## Part II

file = "day_02_input.txt"
fh = open(file, 'r')

checksum = 0

for line in fh:
	vals = line.split('\t')
	vals = list(map(int, vals))
	for i in enumerate(vals):
		for j in enumerate(vals):
			if i[0] == j[0]:
				continue
			if i[1] % j[1] == 0:
				# print(i[1], " ", j[1])
				checksum += i[1] / j[1]

print(checksum)				