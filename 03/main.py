#!/usr/bin/env python3

file = "input.txt"

data = [[character for character in line.strip()] for line in open(file, 'r')]


def evaluate(right, down):
	position = 0
	treeCounter = 0
	isSkipped = False
	for line in data[::down]:
		while len(line) <= position:
			line += line
		if line[position] == '#':
			treeCounter += 1
		position += right
	return treeCounter

def task():
	round1 = evaluate(1, 1)
	round2 = evaluate(3, 1)
	round3 = evaluate(5, 1)
	round4 = evaluate(7, 1)
	round5 = evaluate(1, 2)
	
	print("Part 1: " + str(round2))
	print("Part 2: " + str(round1 * round2 * round3* round4* round5))
	
task()