#!/usr/bin/env python3
import itertools

def calculate2020(file):
	data = [int(line.strip()) for line in open(file, 'r')]
	# for task 1, z was removed
	for x,y,z in itertools.combinations(data, 3):
		if x + y + z == 2020:
			return x*y*z
			break

print(calculate2020("input.txt"))