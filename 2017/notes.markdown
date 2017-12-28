# Advent of Code 2017

## Day 3


17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

Pos | x | y
1 | 0 | 
2 | 1 | 0
3 | 1 | 1
4 | 0 | 1
5 | -1 | 1
6 | -1 | 0
7 | -1 | -1
8 | 0 | -1
9 | 1 | -1


1
2 1
1 -1
2 1
1 -1
2 1
1 -1
2 1

3 1
2 -1
3 1
4 1
3 -1
2 -1
3 1
4 1
3 -1
2 -1
3 1
4 1
3 -1
2 -1
3 1
4 1




Each square has the following nums

1 | 2-9 | 8 
2 | 10-25 | 16
3 | 26-49 | 24
4 | 50-| 32
5 | | 

Square | Dims of each square | Numbers in each square
1 | 3 | 8
2 | 5 | 16
3 | 7 | 24
4 | 9 | 32
5 | 11 | 40

Side lengths dim per square n
sl(n) = 1 + 2n

Numbers in square with side lengths dim:
num(sl) = (sl - 2) * 4 + 4 = 4sl - 8 + 4 = 4(sl) - 4
num(n) = 4 (1 + 2n) - 4 = 4 + 8n - 4 = 8n

Minimum number in square n:
min(n) = 8 * (n - 1) + 8 * (n - 2) + .. + 8 * (1) + 2

8 * 1 + 8 * 2 + 8 * 3 = 8 * (1 + 2 + 3)


range(n) = ( sum( range(i)) for i in 1 to n-1 ) + 1

### Day 7

* Algo
	
	read in nodes to dict
	find root by looking with node name not in any child list
	build tree starting with root:
		Add root node
		From child names, add child nodes (repeat)

		a
	   / \
	  b   c
	 / \ / \
	e  f g  h

### Day 10

0 1 2 3 4
2 1 0 3 4
4 3 0 1 2
4 3 0 1 2
3 4 2 1 0

### Day 11

Use point grid with 0.5 increments to represent hex grid

Distances

(1.5, 2.5) 4

### Day 13

0 0 1
1 1 2
2 2 3
3 3 2
4 2 1
5 1 0
6 0 1
7 1 2
8 2 3

### Day 16

* Dance
	* `__init__`
		* Create from file or with step set
		* From steps, generates a mapping with `getMapping`
	* `applyDance(self, group)`
		* Apply dance to group
	* `getMapping()`
		* Gets a mapping
	* `spin`/`exchange`/`partner`
		* Performs dance moves
		* Utilized by `getMapping` to gen mapping
	* `fromRep(dance, n)`
		* `@staticmethod`
		* Generates a new Dance with mapping corresponding to applying `dance` `n` times

* DanceGroup
	* `__init__`
		* Creates and initializes
	* `applyDance(dance)`
		* Applies dance to the dancegroup

* Logic
	* Find cycle in permutations
	* Solution is 

### Day 17
2nd | Len
1
2
2
2
5
5
5
5
9

* Submitted: 1222153 (too low)

### Day 22



(-1, -1) (-1, 0) (-1, 1)
( 0, -1) ( 0, 0) ( 0, 1)
( 1, -1) ( 1, 0) ( 1, 1)

### Day 23

#### Full
b = 99
c = 9
if a != 0:
	b = b * 100
	b = b + 100000
	c = b
	c = c + 17000
do:
	f = 1
	d = 2
	do:
		e = 2
		do:
			g = d
			g = g * e
			g = g - b
			if g != 0:
				f = 0
			e = e + 1
			g = e
			g = g - b
		: while g != 0
		d = d + 1
		g = d
		g = g - b
	: while g != 0
	if f == 0:
		h = h + 1
	g = b
	g = g - c
	b = b + 17
: while g != 0


#### Simplified
a = 1
<!-- b = 99 -->
<!-- c = 9 -->
<!-- b = 9900  b = b * 100 -->
b = 109900 <!-- b = b + 100000 -->
<!-- c = 109900 c = b -->
c = 126900 <!-- c = c + 17000 -->
do:
	f = 1
	d = 2
	do:
		e = 2
		do:
			<!-- g = 2 g = d -->
			<!-- g = 2e g = g * e -->
			g = 2e - 109900 <!-- g = g - b -->
			if g != 0:
				f = 0
			e = e + 1
			g = e - b <!-- g = e -->
			<!-- g = g - b -->
		: while g != 0
		d = d + 1
		g = d
		g = g - b
	: while g != 0
	if f == 0:
		h = h + 1
	g = b
	g = g - c
	b = b + 17
: while g != 0


h = 0
b = 109900
c = 126900
while True:
	f = 1
	d = 2
	while True:
		e = 2
		while True:
			if (2 * e - 109900 ) == 0:
				f = 0
			e += 1
			if (e - b) == 0:
				break
		d += 1
		if (d - b) == 0:
			break
	if f == 0:
		h += 1
	if (b - c) == 0:
		break
	b = b + 17
	print(h)
print(h)


h = 0
b = 109900
c = 126900
while True:
	f = 1
	d = 2
	while True:
		e = 2
		while True:
			if (d * e - b ) == 0:
				f = 0
			e += 1
			if (e - b) == 0:
				break
		d += 1
		if (d - b) == 0:
			break
	if f == 0:
		h += 1
	if (b - c) == 0:
		break
	b += 17
	print(h)
print(h)


h = 0
b = 109900
c = 126900
while True:
	f = 1
	d = 2	
	while True:
		if b % d == 0:
			f = 0
		d += 1	
		if d == b:
			break
	if f == 0:
		h += 1
	if c == b:
		break
	b += 17
	print(h)
print(h)
					

501 -> too low
1001 -> ?

d * e == b








