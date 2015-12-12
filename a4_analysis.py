#!/usr/bin/env python

# USAGE: 
# Michael Chambers, 2015

import md5, re

key = "bgvyzdsv"
basehash = md5.new()
basehash.update(key)

regex = re.compile("00000")

i = 0
while True:
	i += 1
	m = basehash.copy()
	m.update(str(i))
	shash = str(m.hexdigest())
	hashMatch = regex.match(shash)
	if hashMatch != None:
		print "Match %s with %i" % (shash, i)

