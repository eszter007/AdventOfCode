#!/usr/bin/env python3

file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

directions = []
for d in data:
	tup = (d[0], int(d[1:]))
	directions.append(tup)
	
eastShip = 0
northShip = 0
wayPointEast = 10
wayPointNorth = 1

for direction in directions:
	if direction[0] == "N":
		wayPointNorth += direction[1]
	elif direction[0] == "S":
		wayPointNorth -= direction[1]
	elif direction[0] == "E":
		wayPointEast += direction[1]
	elif direction[0] == "W":
		wayPointEast -= direction[1]
	elif direction[0] == "R":
		moveTimes = direction[1]/90
		while moveTimes != 0:
			newEast = wayPointNorth
			newNorth = -wayPointEast
			wayPointEast = newEast
			wayPointNorth = newNorth
			moveTimes -= 1
	elif direction[0] == "L":
		moveTimes = direction[1]/90
		while moveTimes != 0:
			newEast = -wayPointNorth
			newNorth = wayPointEast
			wayPointEast = newEast
			wayPointNorth = newNorth
			moveTimes -= 1
	elif direction[0] == "F":
		northShip += direction[1]*wayPointNorth
		eastShip += direction[1]*wayPointEast

print(abs(northShip) + abs(eastShip))
