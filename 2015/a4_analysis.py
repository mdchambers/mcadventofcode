#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2015

import hashlib, re

key = b"bgvyzdsv"
basehash = hashlib.md5()
basehash.update(key)

regex = re.compile("00000")

i = 0
while True:
	i += 1
	m = basehash.copy()
	m.update(str(i).encode("utf_8"))
	shash = str(m.hexdigest())
	hashMatch = regex.match(shash)
	if hashMatch != None:
		print("Match ", shash, " with ", i)
		break

#Part 2
key = b"bgvyzdsv"
basehash = hashlib.md5()
basehash.update(key)

regex = re.compile("000000")

i = 0
while True:
	i += 1
	m = basehash.copy()
	m.update(str(i).encode("utf_8"))
	shash = str(m.hexdigest())
	hashMatch = regex.match(shash)
	if hashMatch != None:
		print("Match 2 ", shash, " with ", i)
		break