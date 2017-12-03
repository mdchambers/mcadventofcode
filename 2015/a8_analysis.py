#!/usr/bin/env python

# USAGE: a8_analysis.py
# Michael Chambers, 2015
import re

myFile = "a8_input.txt"
myFH = open(myFile, 'r')

rawTotal = 0
proTotal = 0
while True:
	line = myFH.readline().rstrip()
	if not line: break
	rawTotal += len(line)
	proTotal += len(eval(line))

difTotal = rawTotal - proTotal
print("Raw char: ", rawTotal, "\nInterp total: ", proTotal, "\nDifference: ", difTotal)


#####
# Part 2

x = r"\"abc\""

qre = re.compile(r"[\'\"]")
len(qre.findall(x))

def totalChar(s):
	# Original
	oadd = len(s) + 2
	# Plus 4 for outside quotes
	final = oadd + 4
	# Plus 2 for each inside quote
	qre = re.compile(r"\\[\'\"]")
	final += len(qre.findall(x))
	
	# Plus 1 per \xXX
	xre = re.compile(r"\\x")
	final += len(qre.findall(x))
	print("For string: ", s, " orig: ", oadd, " final: ", final)

totalChar(r"")
totalChar(r"abc")
totalChar("aaa\"aaa")
totalChar(r"aaa\"aaa")
totalChar(r"\x27")

mfh = open("a8_input.txt", 'r')