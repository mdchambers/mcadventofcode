#!/usr/bin/env python

# USAGE: a6_analysis.py
# Michael Chambers, 2015
import numpy, re

class grid(object):
	def __init__(self, size):
		self.lights = numpy.zeros((size, size), dtype = numpy.int)

	def turnon(self, coord1, coord2):
		self.lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] = 1

	def turnoff(self, coord1, coord2):
		self.lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] = 0

	def toggle(self, coord1, coord2):
		for i in range( coord1[0], coord2[0] + 1):
			for j in range(coord1[1], coord2[1] + 1):
				if self.lights[i,j] == 0:
					self.lights[i,j] = 1
				else:
					self.lights[i,j] = 0

	def printLights(self):
		print(self.lights)

	def sumLights(self):
		return(sum(sum(self.lights)))


x = grid(1000)

cre = re.compile(r"(\d+,\d+)")
mfile = open("a6_input.txt")
while True:
	line = mfile.readline().rstrip()
	if not line: break
	coords = cre.findall(line)
	coord1 = coords[0].split(",")
	coord1 = list(map(int, coord1))
	coord2 = coords[1].split(",")
	coord2 = list(map(int, coord2))
	# print(coord1, coord2)
	if "turn on" in line:
		x.turnon(coord1, coord2)
	elif "turn off" in line:
		x.turnoff(coord1, coord2)
	elif "toggle" in line:
		x.toggle(coord1, coord2)

print("P1: ", x.sumLights())


########
# Part 2
class newgrid(object):
	def __init__(self, size):
		self.lights = numpy.zeros((size, size), dtype = numpy.int)

	def turnon(self, coord1, coord2):
		self.lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] += 1

	def turnoff(self, coord1, coord2):
		self.lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] -= 1
		self.lights[self.lights < 0] = 0

	def toggle(self, coord1, coord2):
		self.lights[coord1[0]:coord2[0]+1, coord1[1]:coord2[1]+1] += 2


	def printLights(self):
		print(self.lights)

	def sumLights(self):
		return(sum(sum(self.lights)))


x = newgrid(1000)

cre = re.compile(r"(\d+,\d+)")
mfile = open("a6_input.txt")
while True:
	line = mfile.readline().rstrip()
	if not line: break
	coords = cre.findall(line)
	coord1 = coords[0].split(",")
	coord1 = list(map(int, coord1))
	coord2 = coords[1].split(",")
	coord2 = list(map(int, coord2))
	# print(coord1, coord2)
	if "turn on" in line:
		x.turnon(coord1, coord2)
	elif "turn off" in line:
		x.turnoff(coord1, coord2)
	elif "toggle" in line:
		x.toggle(coord1, coord2)

print("P2: ", x.sumLights())





