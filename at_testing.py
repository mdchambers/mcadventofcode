#!/usr/bin/env python

# USAGE: at_testing.py
# Michael Chambers, 2014

import re

sub = "this is a match"
sub2 = "not a this match"

mre = re.compile("this")

x = mre.match(sub)
y = mre.match(sub2)

print x.group()
print y.group()