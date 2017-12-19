#!/usr/bin/env python

# USAGE: day_02_01.py
# Michael Chambers, 2015


class RecKeyPress(object):
	def __init__(self, startpos):
		self.keys = [[1,4,7],[2,5,8],[3,6,9]]
		self.pos = startpos

	def move(self, mdir):
		if mdir == "U":
			newpos = (self.pos[0], self.pos[1] - 1)
		elif mdir == "D":
			newpos = (self.pos[0], self.pos[1] + 1)
		elif mdir == "L":
			newpos = (self.pos[0] - 1, self.pos[1])
		elif mdir == "R":
			newpos = (self.pos[0] + 1, self.pos[1])

		if newpos[0] < 0 or newpos[0] > 2 or newpos[1] < 0 or newpos[1] > 2:
			return
		else:
			self.pos = newpos

	def getLocation(self):
		return self.keys[self.pos[0]][self.pos[1]]

class DiagKeyPress(object):
	def __init__(self, startpos):
		self.keys = [[0,0,5,0,0],[0,"A",6,2,0],["D","B",7,3,1],[0,"C",8,4],[0,0,9,0,0]]
		self.pos = startpos

	def move(self, mdir):
		if mdir == "U":
			newpos = (self.pos[0], self.pos[1] + 1)
		elif mdir == "D":
			newpos = (self.pos[0], self.pos[1] - 1)
		elif mdir == "L":
			newpos = (self.pos[0] - 1, self.pos[1])
		elif mdir == "R":
			newpos = (self.pos[0] + 1, self.pos[1])

		if newpos[0] < -2 or newpos[0] > 2 or newpos[1] < -2 or newpos[1] > 2:
			return
		elif abs(newpos[0]) + abs(newpos[1]) >= 3:
			return
		else:
			self.pos = newpos

	def getLocation(self):
		keymap = (self.pos[0] + 2, self.pos[1] + 2)
		# print("{} {}".format(self.pos, keymap))
		return self.keys[keymap[0]][keymap[1]]



def main():
	file = "day_02_input.txt"
	# file = "day_02_test.txt"
	fo = open(file, 'r')
	code = ""
	key = RecKeyPress((1,1))
	for line in fo:
		line = line.strip()
		for movement in line:
			key.move(movement)
			# print("{} {} {}".format(movement, key.pos, key.getLocation()))
		code += format(key.getLocation())
	print(code)
	fo.close()

	## Part 2
	fo = open(file, 'r')
	key = DiagKeyPress((-2, 0))
	code = ""
	for line in fo:
		line = line.strip()
		for movement in line:
			key.move(movement)
			print("{} {} {}".format(movement, key.pos, key.getLocation()))
		code += format(key.getLocation())
		print("---")
	print(code)
	fo.close()






if __name__ == '__main__':
	main()