#!/usr/bin/env python

# USAGE: day_07_01.py
# Michael Chambers, 2015

import re

def main():
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

	### Part 2
	# file = "day_07_input.txt"
	file = "day_07_test.txt"

	matchcount = 0
	with open(file, 'r') as fo:
		for line in fo:
			line = line.rstrip()
			hypertext = re.findall(r"\[[^]]*\]", line)
			supertext = line
			for h in hypertext:
				supertext = supertext.replace(h, "!")
			supertext = supertext.split("!")
			# print(line)
			# print(hypertext)
			# print(supertext)

			valid = False

			bab = list()
			for h in hypertext:
				m = re.search(r"(.)(.)\1", h)
				if m and m.group(1) != m.group(2):
					bab.append(m.group())
			for g in bab:
				restr = g[1] + g[0] + g[1]
				for s in supertext:
					m = re.search(restr, s)
					if m:
						print("Valid {} {} {} {}".format(line, g, s, restr))
						valid = True
			if valid:
				matchcount += 1
	print("Found {}".format(matchcount))


if __name__ == '__main__':
	main()







