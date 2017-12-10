#!/usr/bin/env python

# USAGE: day_09_01.py
# Michael Chambers, 2015

from collections import defaultdict

file = "day_09_input.txt"
stream = open(file, 'r').read().rstrip()

# stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
# stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

scoreCounts = defaultdict(int)

currentScore = 0
level = 0
negated = False
inGarbage = False
garbCount = 0
for s in stream:
	if inGarbage and s != "!" and not negated:
		garbCount += 1
	if negated:
		negated = False
		continue
	if s == "{" and not inGarbage:
		currentScore += 1
		scoreCounts[currentScore] += 1
	elif s == "}" and not inGarbage:
		currentScore -= 1
	elif s == "<":
		inGarbage = True
	elif s == ">" and inGarbage:
		inGarbage = False
		garbCount -= 1
	elif s == "!":
		negated = True

total = 0
for k,v in scoreCounts.items():
	print ("key: {} val: {}".format(k,v))
	total += k * v
print("Total: {}".format(total))
print("Total Garbage Chars: {}".format(garbCount))


