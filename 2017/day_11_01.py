#!/usr/bin/env python

# USAGE: day_11_01.py
# Michael Chambers, 2015

file = "day_11_input.txt"
movements = open(file,'r').read().rstrip()
movements = movements.split(',')

def calcDist(x,y):
	return(abs(x) + abs(y))

posx = 0
posy = 0
maxdist = 0
for m in movements:
	# print(m)
	if m == "n":
		posy += 1
	elif m == "s":
		posy -= 1
	elif m == "ne":
		posx += 0.5
		posy += 0.5
	elif m == "se":
		posx += 0.5
		posy -= 0.5
	elif m == "nw":
		posx -= 0.5
		posy += 0.5
	elif m == "sw":
		posx -= 0.5
		posy -= 0.5
	else:
		print("ERROR")
	cdist = calcDist(posx,posy)
	if cdist > maxdist:
		maxdist = cdist

print("Final coord: {},{}".format(posx, posy))
print("Distance to origin: {}".format(calcDist(posx, posy)))
print("Maximum distance from origin: {}".format(maxdist))