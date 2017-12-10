#!/usr/bin/env python

# USAGE: day_07_01.py
# Michael Chambers, 2015


def parseLine(line):
	ll = line.split(" ")
	name = ll[0]
	weight = int(ll[1].strip("()\n"))
	if "->" in ll:
		children = ll[3:]
		children = list(map(lambda s: s.strip(","), children))
	else:
		children = None
	return (name, weight, children)

class Disk(object):
	def __init__(self, name, diskdict):
		self.name = name
		self.weight = diskdict[name][0]
		if diskdict[name][1] is None:
			self.children = None
		else:
			self.children = list()
			for c in diskdict[name][1]:
				self.children.append(Disk(c, diskdict))

	def printout(self):
		if self.children is not None:
			childNames = list(map(lambda d: d.name, self.children))
		else:
			childNames = ""
		print ("Name: {} Weight: {} Children: {}".format(self.name, self.weight, childNames))

	def getChildWeights(self):
		if self.children is None:
			return(0,)
		cw = list()
		for c in self.children:
			cw.append(c.getChildTotalWeight() + c.weight)
		return(cw)
	
	def getChildTotalWeight(self):
		if self.children is None:
			return(0)
		cw = 0
		for c in self.children:
			totalweight = c.weight + c.getChildTotalWeight()
			cw += totalweight
		return(cw)

	def getDiskByName(self, name):
		# self.printout()
		if self.name == name:
			# print("found")
			return(self)
		if self.children is not None:
			for d in self.children:
				found = d.getDiskByName(name)
				if found is not None:
					return(found)
		return(None)

	def findUnbalanced(self):
		if self.children:
			childweights = self.getChildWeights()
			if len(set(childweights)) > 1:
				unbalanced = True
				print("Unbalanced: ", self.name)
				self.printout()
				print(childweights)
				for d in self.children:
					print(d.name, " ", d.weight)
					d.findUnbalanced()
			else:
				print("Balanced: ", self.name)
		else:
			print("End ", self.name)





file = "day_07_input.txt"
fh = open(file, 'r')

diskdict = dict()
for line in fh:
	# print(line)
	line = line.rstrip()
	lineparse = parseLine(line)
	diskdict[lineparse[0]] = lineparse[1:]

# print(diskdict)
# Find root
for k in diskdict.keys():
	hasparents = False
	for v in diskdict.values():
		if v[1] is None:
			continue
		if k in v[1]:
			# print("found parent for ", k)
			hasparents = True
			break
	if not hasparents:
		print("Found root: ", k)
		root = k
		break

tree = Disk(root, diskdict)

tree.printout()
print(tree.getChildWeights())
print(tree.getChildTotalWeight())

tree.getDiskByName("sbcuc").printout()

tree.findUnbalanced()



# problemProg
