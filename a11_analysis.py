#!/usr/bin/env python

# USAGE: a11_analysis.py
# Michael Chambers, 2015
import string
import re

myInput = "vzbxkghb"

# a = 97
# z = 122

def incrementChar(string, position):	
	# Check if increments
	sl = list(string)
	sl[position] = chr(ord(sl[position]) + 1)
	if ord(sl[position]) > 122:
		sl[position] = 'a'
		if not position == 0:
			sl = incrementChar("".join(sl), position - 1)
	return("".join(sl))


def checkRun(string):
	sl = map(ord, list(string))
	for idx in range(len(sl)):
		if idx + 2 >= len(sl): 
			continue
		if sl[idx] + 1 == sl[idx + 1] and sl[idx] + 2 == sl[idx + 2]:
			return True
	return False

def chrRestriction(string):
	if 'i' in string or 'o' in string or 'l' in string:
		return False
	return True

# Must contain two different non-overlapping pairs
def checkPairs(string):
	nre = re.compile(r"(.)\1")
	matches = nre.findall(string)
	if matches is not None and len(matches) >= 2:
		return True
	return False


cs = myInput
while True:
	cs = incrementChar(cs, len(cs) - 1)
	if checkRun(cs) and chrRestriction(cs) & checkPairs(cs):
		print cs



# ms = "aaaaaaa"
# for i in range(100):
# 	ms = incrementChar(ms, 3)
# 	print "%s %d %d %d" % (ms, checkRun(ms), chrRestriction(ms), checkPairs(ms)) 