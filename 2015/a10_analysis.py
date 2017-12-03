#!/usr/bin/env python

# USAGE: a10_analysis.py
# Michael Chambers, 2015

myInput = "1321131112"
print myInput
for i in range(40):
	currChar = myInput[0]
	currCharCount = 0
	outputString = ''
	for c in myInput:
		# print "%s %s %s %s" % (c, currChar, currCharCount, outputString)
		if currChar == c:
			# print currChar
			currCharCount += 1
		else:
			# Append output string
			# print "Appending %s" % c
			outputString += "%d%s" % (currCharCount, currChar)
			currChar = c
			currCharCount = 1
	outputString += "%d%s" % (currCharCount, currChar)
	# print outputString
	# print ""
	myInput = outputString
# print "foo"
print len(outputString)