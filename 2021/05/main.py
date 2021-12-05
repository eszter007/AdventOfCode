#!/usr/bin/env python3
data = [[[int(number) for number in pair.split(",")] for pair in line] for line in [line.strip().split(" -> ") for line in open("input.txt", 'r')]]

print(data)

def direction(line):
	if line[0][1] == line[1][1]:
		return "h"
	elif line[0][0] == line[1][0]:
		return "v"
	return "d"

matrix = [ [ 0 for i in range(1000) ] for j in range(1000)]

for line in data:
	if direction(line) == "h":
		x1 = line[0][0]
		x2 = line[1][0]
		for i in range(min(x1, x2), max(x1, x2)+1):
			matrix[line[0][1]][i] += 1
	if direction(line) == "v":
		y1 = line[0][1]
		y2 = line[1][1]
		for i in range(min(y1, y2), max(y1, y2)+1):
			matrix[i][line[0][0]] += 1
	
c = 0
for i in matrix:
	for j in i:
		if j >= 2:
			c += 1

print("Answer 1: " + str(c))

for line in data:
	if direction(line) == "d":
		x1 = line[0][0]
		x2 = line[1][0]
		initialY = 0
		signum = 0
		if x1 > x2:
			initialY = line[1][1]
			deltaY = line[0][1] - initialY
			if deltaY > 0: signum = 1 
			else: signum = -1 
		else: 
			initialY = line[0][1]
			deltaY = line[1][1] - initialY
			if deltaY > 0: signum = 1 
			else: signum = -1 
		for i in range(min(x1, x2), max(x1, x2)+1):
			matrix[initialY][i] += 1
			initialY += signum

c = 0
for i in matrix:
	for j in i:
		if j >= 2:
			c += 1
			
print("Answer 2: " + str(c))