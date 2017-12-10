#!/usr/bin/env python

# USAGE: day_08_01.py
# Michael Chambers, 2015

# from collections import defaultdict

# class Command:
# 	def processCondition(self, condition):
# 		self.condition = (condition[0], condition[1], int(condition[2]))

# 	def __init__(self, name, change, value, condition):
# 		self.name = name
# 		self.change = change
# 		self.value = int(value)
# 		self.processCondition(condition)

# 	def __str__(self):
# 		return('Name: {} Change: {} Value: {}, Condition: {}'.format(self.name, self.change, self.value, self.condition))


# def loadRegisters(file):
# 	fh = open(file, 'r')

# 	commands = dict()
# 	for line in fh:
# 		line = line.rstrip()
# 		lsp = line.split()
# 		commands[lsp[0]] = Command(lsp[0], lsp[1],lsp[2], lsp[4:])
# 		# print(commands[lsp[0]])
# 	return(commands)

# def main():
# 	com = loadRegisters("day_08_input.txt")
# 	for k,v in com.items():
# 		print(v)



# if __name__ == "__main__":
# 	main()

from collections import defaultdict

def main():
	file = "day_08_input.txt"
	fh = open(file, 'r')
	registers = defaultdict(int)
	runningMax = 0
	for line in fh:
		line = line.rstrip()
		lsp = line.split()
		name = lsp[0]
		change = lsp[1]
		value = int(lsp[2])
		condition = lsp[4:]
		condition[2] = int(condition[2])

		conditionMet = False
		if condition[1] == "<":
			conditionMet = registers[condition[0]] < condition[2]
		elif condition[1] == "<=":
			conditionMet = registers[condition[0]] <= condition[2]
		elif condition[1] == ">":
			conditionMet = registers[condition[0]] > condition[2]
		elif condition[1] == ">=":
			conditionMet = registers[condition[0]] >= condition[2]
		elif condition[1] == "==":
			conditionMet = registers[condition[0]] == condition[2]
		elif condition [1] == "!=":
			conditionMet = registers[condition[0]] != condition[2]
		if conditionMet:
			if change == "inc":
				registers[name] += value
			elif change == "dec":
				registers[name] -= value
		if registers[name] > runningMax:
			runningMax = registers[name]

	print(max(registers.values()))
	print(runningMax)


if __name__ == "__main__":
	main()





