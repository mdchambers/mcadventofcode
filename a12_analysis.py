#!/usr/bin/env python

# USAGE: a12_analysis.py
# Michael Chambers, 2015

import json
import re

myFile = "a12_input.txt"

mfh = open(myFile, 'r')
js = json.load(mfh)
mfh.close()

pjs = json.dumps(js, sort_keys=True, indent=4, separators=(',', ': '))

ofh = open("a12_pretty_input.json", 'w')
ofh.write(pjs)
ofh.close()
# def traverse(o, tree_types=(list, tuple, dict)):
#     if isinstance(o, tree_types):
#         for value in o:
#             for subvalue in traverse(value, tree_types):
#                 yield subvalue
#     else:
#         yield o

# for i in traverse(js):
# 	print i


mfh = open("a12_pretty_input.json", 'r')

total = 0
while True:
	line = mfh.readline().rstrip()
	if not line: break
	ll = line.split()
	# ll = map(lambda x : x.split(","), ll)
	# ll =

	for i in ll:
		i = i.translate(None, ",")
		print i
		try:
			ii = int(i)
			total += ii
		except ValueError:
			pass
	print total

# total = 0

# mfh = open("a12_input.txt", 'r')
# while True:
# 	line = mfh.readline().rstrip()
# 	if not line: break
# 	ll = re.split(r"{|}|[|]|,|\"", line)
# 	# ll = line.split()
# 	# ll = map(lambda x : x.split(","), ll)
# 	# ll =

# 	for i in ll:
# 		print i
# 	# 	try:
# 	# 		ii = int(i)
# 	# 		total += ii
# 	# 	except ValueError:
# 	# 		pass
# 	# print total
