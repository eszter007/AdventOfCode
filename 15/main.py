#!/usr/bin/env python3

def part1(numbers, spokenNo):
	spoken = dict()
	nextNo = 0
	position = 1
	
	for n in numbers:
		spoken[n] = position
		position += 1
		
	while position <= spokenNo:
		current = nextNo
		if current in spoken: nextNo = position - spoken[current]
		else:
			nextNo = 0
		spoken[current] = position
		position += 1
		
	return current

print("Part 1: " + str(part1([9,19,1,6,0,5,4], 2020)))
print("Part 2: " + str(part1([9,19,1,6,0,5,4], 30000000)))