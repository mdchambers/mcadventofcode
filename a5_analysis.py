#!/usr/bin/env python

# USAGE: a5_analysis.py
# Michael Chambers, 2015

import re

mfile = open("a5_input.txt", 'r')


mre = re.compile(r"[aeiou]")
nre = re.compile(r"(.)\1")
ore = re.compile(r"ab|cd|pq|xy")
# nre = re.compile(".*(.)(?=\1)")
found = 0
while True:
	x = mfile.readline().rstrip()
	if not x: break
	vowels = mre.findall(x)
	if len(vowels) < 3: continue
	if nre.search(x) == None: continue
	if ore.search(x) != None: continue
	print x
	found += 1

print "Found %d matches." % found
	