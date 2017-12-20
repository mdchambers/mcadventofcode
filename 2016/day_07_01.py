#!/usr/bin/env python

# USAGE: day_07_01.py
# Michael Chambers, 2015

import re
import regex

def part1():
	file = "day_07_input.txt"
	# file = "day_07_test.txt"
	matchcount = 0
	with open(file, 'r') as fo:
		for line in fo:
			invalid = False

			line = line.rstrip()
			# print(line)
			hyper = re.findall(r"\[[^]]*\]", line)

			if hyper:
				for h in hyper:
					# print(h)
					m = re.search(r"(.)(.)\2\1", h)
					if m and m.group(1) != m.group(2):
						# print(m.group())
						invalid = True
						continue

			line = re.sub(r"\[[^]]*\]", '!', line)
			# print(line)
			m = re.search(r"(.)(.)\2\1", line)
			if not invalid and m and m.group(1) != m.group(2):
				# print(line)
				# print(m.group())
				# print("Valid")
				matchcount += 1
			# else:
				# print("Invalid or No Match")
			# print("---")
	print("Found {}".format(matchcount))

def part2():
	file = "day_07_input.txt"
	# file = "day_07_test.txt"

	matchcount = 0
	with open(file, 'r') as fo:
		for line in fo:
			line = line.rstrip()
			line = line.replace("[", "!").replace("]", "!")
			ls = line.split("!")
			supertext = list( ls[i] for i in range(0, len(ls), 2))
			hypertext = list( ls[i] for i in range(1, len(ls), 2))
			print("Line: {} Super: {} Hyper: {}".format(line, supertext, hypertext))
			valid = False
			for s in supertext:
				for m in regex.finditer(r'(.)(.)\1', s, overlapped=True):
					if m.group(1) != m.group(2):
						restr = m.group(2) + m.group(1) + m.group(2)
						print(m.group(0), restr)
						for h in hypertext:
							inhyper = re.search(restr, h)
							if inhyper:
								valid = True
								# print("valid")
			if valid:
				matchcount += 1

	print("Found {}".format(matchcount))	

def main():
	part1()
	part2()





if __name__ == '__main__':
	main()



			# line = line.rstrip()
			# hypertext = re.findall(r"\[[^]]*\]", line)
			# supertext = line
			# for h in hypertext:
			# 	supertext = supertext.replace(h, "!")
			# supertext = supertext.split("!")
			# # print(line)
			# # print(hypertext)
			# # print(supertext)

			# valid = False

			# bab = list()
			# for h in hypertext:
			# 	m = re.search(r"(.)(.)\1", h)
			# 	if m and m.group(1) != m.group(2):
			# 		bab.append(m.group())
			# for g in bab:
			# 	restr = g[1] + g[0] + g[1]
			# 	for s in supertext:
			# 		m = re.search(restr, s)
			# 		if m:
			# 			print("Valid {} {}".format(g, restr))
			# 			valid = True
			# if valid:
			# 	matchcount += 1



