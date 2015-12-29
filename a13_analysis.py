#!/usr/bin/env python

# USAGE: a13_analysis.py
# Michael Chambers, 2015
import itertools

myfile = "a13_input.txt"

mfh = open(myfile, 'r')

class Guest(object):
	def __init__(self, name):
		self.name = name
		self.relationship = dict()

	def addRelationship(self, name, happiness):
		self.relationship[name] = happiness

	def getHappiness(self, lName, rName):
		return self.relationship[lName] + self.relationship[rName]

	def printRelationships(self):
		for k, v in self.relationship.items():
			print(k, v)

class Seating(object):
	def __init__(self, order):
		# self.guests = guests
		self.order = order

	def getHappiness(self, allGuests):
		happys = 0
		for idx in range(len(self.order)):
			if idx == 0:
				lpos = len(self.order) - 1
			else:
				lpos = idx - 1
			if idx == len(self.order) - 1:
				rpos = 0
			else:
				rpos = idx + 1
			# print(lpos, idx, rpos, len(self.order))
			lname  = self.order[lpos]
			cname  = self.order[idx]
			cguest = allGuests[cname]
			rname = self.order[rpos]
			happys += cguest.getHappiness(lname, rname)
		return happys

def constructGuests(gfile):
	mfh = open(gfile, 'r')
	guests = dict()
	while True:
		line = mfh.readline().rstrip(".\n")
		if not line: break
		ll = line.split()
		lname = ll[0]
		rname = ll[10]
		val = int(ll[3])
		if ll[2] == "lose":
			val = - val
		if not lname in guests:
			guests[lname] = Guest(lname)
		guests[lname].addRelationship(rname, val)
	return(guests)

allGuests = constructGuests("a13_input.txt")

# for k, v in allGuests.items():
# 	v.printRelationships()

guestIter = itertools.permutations(allGuests.keys())

hap = list()
for gi in guestIter:
	# print(gi)
	seat = Seating(gi)
	hap.append(seat.getHappiness(allGuests))

print(max(hap))

###
# Part 2
allGuests = constructGuests("a13_input2.txt")

guestIter = itertools.permutations(allGuests.keys())

hap = list()
for gi in guestIter:
	# print(gi)
	seat = Seating(gi)
	hap.append(seat.getHappiness(allGuests))

print(max(hap))

