#!/usr/bin/env python3

data = [line.strip().split(" ") for line in open("input.txt", 'r')]

def calculate(isAim):
	horizontalPos = 0
	depth = 0
	aim = 0
	forward = "forward"
	down =  "down"
	up = "up"
	for line in data:
		if not isAim:
			if line [0] == forward:
				horizontalPos += int(line[1])
			elif line [0] == down:
				depth += int(line[1])
			elif line [0] == up:
				depth -= int(line[1])
		else:
			if line [0] == forward:
				horizontalPos += int(line[1])
				depth += aim * int(line[1])
			elif line [0] == down:
				aim += int(line[1])
			elif line [0] == up:
				aim -= int(line[1])
	return depth * horizontalPos

# Task 1
print("Task 1: " + str(calculate(False)))

# Task 2
print("Task 2: " + str(calculate(True)))
