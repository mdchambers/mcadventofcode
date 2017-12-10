#!/usr/bin/env python

# USAGE: day_10_01.py
# Michael Chambers, 2015
from itertools import chain
from functools import reduce

lengths = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"
lengths = lengths.split(",")
lengths = list(map(int, lengths))

mlist = list(range(256))

# mlist = list(range(5))
# lengths = (3,4,1,5)

pos = 0
skip = 0
for l in lengths:
	while pos >= len(mlist):
		pos = pos - len(mlist)
	startRev = pos
	endRev = startRev + l - 1
	if endRev >= len(mlist):
		endRev = endRev - len(mlist)
		revSection = list(chain(mlist[startRev:], mlist[:endRev + 1]))
		revSection = list(reversed(revSection))
		outList = list(chain(revSection[len(mlist) - startRev:], mlist[endRev + 1: startRev], revSection[:len(mlist) - startRev]))
	else:
		revSection = list(reversed(mlist[startRev:endRev + 1]))
		outList = list(chain(mlist[:startRev], revSection, mlist[endRev +1:]))
	mlist = outList
	pos = pos + l + skip
	skip += 1

print("First two product: {}".format(mlist[0] * mlist[1]))


### Part 2

def denseHash(sparse):
	dense = list()
	for i in range(0, 255, 16):
		seti = sparse[i:i+16]
		red = reduce(lambda x,y: x ^ y, seti)
		# print("xoring {} {} {}".format(seti, len(seti), red))
		dense.append(red)
	# print("Dense hash: {}".format(dense))

	mhash = ''.join(["{:02x}".format(x) for x in dense])	
	return(mhash)

lengths = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"
# lengths = "1,2,4"
lengths = list(map(ord, lengths))
lengths = list(chain(lengths, [17, 31, 73, 47, 23]))
print(lengths)

mlist = list(range(256))
pos = 0
skip = 0
for i in range(64):
	# mlist = list(range(256))
	for l in lengths:
		while pos >= len(mlist):
			# print("resetting pos from {} to {}".format(pos, pos - len(mlist)))
			pos = pos - len(mlist)
		startRev = pos
		endRev = startRev + l - 1

		if endRev >= len(mlist):
			endRev = endRev - len(mlist)
			revSection = list(chain(mlist[startRev:], mlist[:endRev + 1]))
			revSection = list(reversed(revSection))
			outList = list(chain(revSection[len(mlist) - startRev:], mlist[endRev + 1: startRev], revSection[:len(mlist) - startRev]))
		else:
			revSection = list(reversed(mlist[startRev:endRev + 1]))
			outList = list(chain(mlist[:startRev], revSection, mlist[endRev +1:]))
		mlist = outList
		pos = pos + l + skip
		skip += 1
		# print("Curr List: {}".format(mlist))
	print(denseHash(mlist))

# print(denseHash(list(range(256))))


