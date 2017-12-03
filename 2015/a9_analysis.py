#!/usr/bin/env python

# USAGE: a9_analysis.py
# Michael Chambers, 2015

# Let's bruteforce it
# There should be 8! ~= 40,000 possible tours, should be doable

import itertools

class City(object):
	def __init__(self, name):
		self.name = name
		self.routes = dict()

	def addRoute(self, destination, distance):
		self.routes[destination] = int(distance)

	def getDistance(self, destination):
		return(self.routes[destination])
		

class CityMap(object):
	def __init__(self, inFile):
		# myFile = inFile
		myFH = open(inFile)
		self.cityList = set()
		self.cities   = dict()
		while True:
			line  = myFH.readline().rstrip()
			if not line: break
			ll    = line.split()
			cityA = ll[0]
			cityB = ll[2]
			dist  = ll[4]
			
			self.cityList.add(cityA)
			self.cityList.add(cityB)

			if not cityA in self.cities.keys():
				self.cities[cityA] = City(cityA)
			if not cityB in self.cities.keys():
				self.cities[cityB] = City(cityB)
			self.cities[cityB].addRoute(cityA, dist)
			self.cities[cityA].addRoute(cityB, dist)

	def getSize(self):
		return(len(self.cityList))

	def getDistance(self, origin, destination):
		return(self.cities[origin].getDistance(destination))

	def getRouteDist(self):
		pert = itertools.permutations(self.cityList, len(self.cityList))
		distances = list()
		for r in pert:
			totalDist = 0
			for idx, val in enumerate(r):
				if idx + 1 < len(r):
					totalDist += self.getDistance(r[idx], r[idx + 1])
				# print self.getDistance(val, r[idx + 1])
			distances.append(totalDist)
			print totalDist
		print min(distances)



myNet = CityMap("a9_input.txt")

# print myNet.getSize()
# print myNet.getDistance('Straylight', 'Arbre')
myNet.getRouteDist()