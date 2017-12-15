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



