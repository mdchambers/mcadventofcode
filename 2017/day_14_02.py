#!/usr/bin/env python

# USAGE: day_14_01.py
# Takes about 5.8 sec
# Michael Chambers, 2015

from functools import reduce

def sparseHash(inputstr):
	lengths = inputstr
	lengths = list(map(ord, lengths))
	lengths = lengths + [17, 31, 73, 47, 23]

	mlist = list(range(256))
	pos = 0
	skip = 0
	for i in range(64):
		for l in lengths:
			while pos >= len(mlist):
				pos = pos - len(mlist)
			startRev = pos
			endRev = startRev + l - 1

			if endRev >= len(mlist):
				endRev = endRev - len(mlist)
				revSection = mlist[startRev:] + mlist[:endRev + 1]
				revSection = list(reversed(revSection))
				# print("{} {}".format(type(revSection), type(mlist)))
				outList = revSection[len(mlist) - startRev:] + mlist[endRev + 1: startRev] + revSection[:len(mlist) - startRev]
			else:
				revSection = list(reversed(mlist[startRev:endRev + 1]))
				outList = mlist[:startRev] + revSection + mlist[endRev +1:]
			mlist = outList
			pos = pos + l + skip
			skip += 1
	return(mlist)

def denseHash(sparse):
	dense = list()
	for i in range(0, 255, 16):
		seti = sparse[i:i+16]
		red = reduce(lambda x,y: x ^ y, seti)
		dense.append(red)

	mhash = ''.join(["{:02x}".format(x) for x in dense])	

	return(mhash)

def bitHash(dense):
	bit = ""
	for d in dense:
		di = int(d, 16)
		db = format(di, "04b")
		bit += db
	return(bit)
		
def sumBits(hlist):
	bsum = 0
	for h in hlist:
		bsum += h.count("1")
	return(bsum)

def toBitGrid(blist):
	bg = list()
	for i in blist:
		bline = list(map(int, list(i)))
		bg.append(bline)
	return(bg)

def printGrid(grid, x, y):
	for i in range(x):
		mystr = ''.join("{:3} ".format(v) for v in grid[i][:y])
		print(mystr)
	print("---")

def connectedCells(grid, cell, currset):
	x = cell[0]
	y = cell[1]
	toadd = set()
	if x > 0 and grid[x - 1][y] == 1:
		toadd.add((x - 1,y))
	if x + 1 < len(grid) and grid[x + 1][y] == 1:
		toadd.add((x + 1, y))
	if y > 0 and grid[x][y - 1] == 1:
		toadd.add((x, y - 1))
	if y + 1 < len(grid[x]) and grid[x][y + 1] == 1:
		toadd.add((x, y + 1))		
	for c in toadd:
		if c not in currset:
			currset.add(c)
			# print("Recursing into {} for cell {}".format(c, cell))
			toadd = toadd | connectedCells(grid, c, currset)
	currset = currset | toadd | set([cell])
	return(currset)


def main():
	minput = "vbqugkhl"
	# minput = "flqrgnkx"

	bithashes = list()
	for i in range(128):
		linekey = minput + "-" + str(i)
		sh = sparseHash(linekey)
		# print(sh)
		dh = denseHash(sh)
		# print("Linekey {} Hash {}".format(linekey, dh))
		bh = bitHash(dh)
		# print(len(bh))
		bithashes.append(bh)
	# for i in range(8):
		# print(hashes[i][:8])

	print("Sum of bits: {}".format(sumBits(bithashes)))

	bitgrid = toBitGrid(bithashes)

	printGrid(bitgrid, 10, 10)

	connections = list()
	for i in range(len(bitgrid)):
		for j in range(len(bitgrid)):
			if bitgrid[i][j] == 1:
				connections.append(connectedCells(bitgrid, (i,j), set()))

	print("Total nonunique groups: {}".format(len(connections)))


	uniquesets = set(tuple(sorted(x)) for x in connections)
	print("Unique groups {}".format(len(uniquesets)))

	numgrid = [[0 for x in range(128)] for y in range(128)]
	for i, s in enumerate(uniquesets):
		for cell in s:
			numgrid[cell[0]][cell[1]] = i + 1
	printGrid(numgrid, 10, 10)



if __name__ == '__main__':
	main()





