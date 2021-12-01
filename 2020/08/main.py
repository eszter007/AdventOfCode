#!/usr/bin/env python3
from copy import deepcopy

file = "input.txt"
def format (line):
	tup = line.strip().split(" ")
	return [tup[0], int(tup[1])]
data = [format(line) for line in open(file, 'r')]

def alg(program):
	index = 0
	acc = 0
	visited = {index}
	visitedTwice = False
	
	while True:
		current = program[index]
		if current[0] == "nop":
			index += 1
		elif current[0] == "acc": 
			acc += current[1]
			index += 1
		elif current[0] == "jmp":
			index += current[1]
		if index in visited:
			visitedTwice = True
		else: visited.add(index)
		if visitedTwice:
			return acc, True
		elif index >= len(data):
			return acc, False

def part1():
	acc = alg(data)
	print("Part 1: " + str(acc[0]))
	
part1()

def part2():
	for i in range(0, len(data)):
		dataCopy = deepcopy(data)
		if dataCopy[i][0] == "nop":
			dataCopy[i][0] = "jmp"
		elif dataCopy[i][0] == "jmp": 
			dataCopy[i][0] = "nop"
		candiate = alg(dataCopy)
		if candiate[1] == False:
			return candiate[0]
		
print("Part 2: " + str(part2()))
