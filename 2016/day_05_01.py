#!/usr/bin/env python

# USAGE: day_05_01.py
# Michael Chambers, 2015

import hashlib

def getHash(mstring):
	m = hashlib.md5()
	m.update(mstring.encode())
	return(m.hexdigest())

def part1(minput):
	index = 0
	password = ""
	while True:
		tohash = minput + format(index)
		currhash = getHash(tohash)
		if currhash[:5] == "00000":
			password += currhash[5]
			print("Found code {} at index {}".format(password, index))
		index += 1
		if len(password) >= 8:
			break
		if index % 100000 == 0:
			print("Processing index {}".format(index))
	print("Password is {}".format(password))

def part2(minput):
	index = 0
	password = ["_"] * 8
	while True:
		tohash = minput + format(index)
		currhash = getHash(tohash)
		if currhash[:5] == "00000":
			if int(currhash[5], 16) <= 7:
				if password[int(currhash[5], 16)] == "_":
					password[int(currhash[5], 16)] = currhash[6]
					print("Found code {} at index {}".format(password, index))
					if "_" not in password:
						break
		index += 1
		if index % 100000 == 0:
			print("Processing index {}".format(index))
	pwdstr = ''.join(password)
	print("Password is {}".format(pwdstr))

def main():
	minput = "uqwqemis"
	# minput = "abc"

	# part1(minput)
	part2(minput)




if __name__ == '__main__':
	main()