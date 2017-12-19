#!/usr/bin/env python

# USAGE: day_17_01.py
# Michael Chambers, 2017

class Spinlock:
	def __init__(self, step):
		self.step = step
		self.buffer = [0]
		self.pos = 0
		self.rep = 0 

	def addValue(self):
		# self.pos = (self.pos + self.step) % len(self.buffer)
		self.pos = self.pos + self.step
		while self.pos >= len(self.buffer):
			self.pos = self.pos - len(self.buffer)
			# print("rollback")
		self.rep += 1
		# if self.pos == 0:
			# self.buffer = [self.buffer[0]] + [self.rep] + self.buffer[1:]
		# else:
		self.buffer = self.buffer[:self.pos + 1] + [self.rep] + self.buffer[self.pos + 1:]
		# print(self.buffer[:self.pos], self.rep, self.buffer[self.pos:])
		self.pos += 1



	def getValueAfterInsertion(self, n):
		while self.rep <= n:
			self.addValue()
			# if self.rep % 100000 == 0:
				# print("On step: {}".format(self.rep))
			# print(self.rep)
		if self.pos + 1 >= len(self.buffer):
			return(self.buffer[0])
		else:
			return(self.buffer[self.pos + 1])


	def __str__(self):
		# outstr = ''.join(self.buffer)
		return("Step: {} Pos: {} Rep: {}\n{}".format(self.step, self.pos, self.rep, self.buffer))
	

def fastSpin(step, cycles):
	spinlen = 2
	twopos = 1
	pos = 1
	while spinlen < cycles:
		pos = (pos + step) % spinlen
		if pos == 0:
			twopos = spinlen
			print(twopos)
		# print("Len: {} Pos: {} Second: {}".format(spinlen, pos, twopos))
		spinlen += 1
		pos += 1
		if spinlen % 100000 == 0:
			print("Cycle: {}".format(spinlen))
	print(twopos)



def main():
	# step = 3
	step = 337
	sl = Spinlock(step)
	outval = sl.getValueAfterInsertion(2016)
	# print(sl)
	print(outval)
	# finalindex = sl.buffer.index(20)
	# print(sl.buffer[finalindex-2:finalindex+2])
	# part2 = Spinlock(step)
	# outval = sl.getValueAfterInsertion(49999999)
	# print(outval)
	# print(sl.buffer[:5])
	# fastSpin(step, 10)
	fastSpin(step, 50000000)



if __name__ == "__main__":
	main()

