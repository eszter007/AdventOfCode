#!/usr/bin/env python3
from copy import deepcopy
import numpy as np

file = "input.txt"
data = [list(line.strip()) for line in open(file, 'r')]

"""
------Part 1-------
"""

def getNeighbors(row, column, matrix):
	seatsAround = []
	# top left
	if row == 0 and column == 0:
		# right seat
		seatsAround.append(matrix[row][column + 1])
		#diagonal right seat
		seatsAround.append(matrix[row + 1][column + 1])
		#seat under
		seatsAround.append(matrix[row + 1][column])
		
	# bottom left
	elif row == len(matrix)-1 and column == 0:
		# right seat
		seatsAround.append(matrix[row][column + 1])
		#diagonal right seat above
		seatsAround.append(matrix[row - 1][column + 1])
		#seat above
		seatsAround.append(matrix[row - 1][column])
		
	# top right
	elif row == 0 and column == len(matrix[row])-1:
		# left seat
		seatsAround.append(matrix[row][column - 1])
		# left seat diagonal underneath
		seatsAround.append(matrix[row + 1][column - 1])
		# underneath
		seatsAround.append(matrix[row + 1][column])
		
	# bottom right	
	elif row == len(matrix)-1 and column == len(matrix[row])-1:
		# above seat
		seatsAround.append(matrix[row - 1][column])
		# above diagonal left seat
		seatsAround.append(matrix[row - 1][column - 1])
		# left seat
		seatsAround.append(matrix[row][column - 1])
	
	# right
	elif column == len(matrix[row])-1 and row != 0 and row < len(matrix)-1:
		# above seat
		seatsAround.append(matrix[row - 1][column])
		# undernath seat
		seatsAround.append(matrix[row + 1][column])
		# left seat
		seatsAround.append(matrix[row][column - 1])
		# diagonal above left seat
		seatsAround.append(matrix[row - 1][column - 1])
		# diagonal underneath left seat
		seatsAround.append(matrix[row + 1][column - 1])
	
	# left
	elif column == 0:
		# above seat
		seatsAround.append(matrix[row - 1][column])
		# undernath seat
		seatsAround.append(matrix[row + 1][column])
		# right seat
		seatsAround.append(matrix[row][column + 1])
		# diagonal above right seat
		seatsAround.append(matrix[row - 1][column + 1])
		# diagonal underneath right seat
		seatsAround.append(matrix[row + 1][column + 1])
	
	# bottom
	elif row == len(matrix)-1 and column < len(matrix[row])-1:
		# above seat
		seatsAround.append(matrix[row - 1][column])
		# right seat
		seatsAround.append(matrix[row][column + 1])
		# left seat
		seatsAround.append(matrix[row][column - 1])
		# diagonal above right seat
		seatsAround.append(matrix[row - 1][column + 1])
		# diagonal above left seat
		seatsAround.append(matrix[row - 1][column - 1])
	
	# top
	elif row == 0:
		# undernath seat
		seatsAround.append(matrix[row + 1][column])
		# right seat
		seatsAround.append(matrix[row][column + 1])
		# left seat
		seatsAround.append(matrix[row][column - 1])
		# diagonal underneath right seat
		seatsAround.append(matrix[row + 1][column + 1])
		# diagonal underneath left seat
		seatsAround.append(matrix[row + 1][column - 1])
	
	else:
		# above seat
		seatsAround.append(matrix[row - 1][column])
		# underneath seat
		seatsAround.append(matrix[row + 1][column])
		# right seat
		seatsAround.append(matrix[row][column + 1])
		# left seat
		seatsAround.append(matrix[row][column - 1])
		# diagonal above right seat
		seatsAround.append(matrix[row - 1][column + 1])
		# diagonal above left seat
		seatsAround.append(matrix[row - 1][column - 1])
		# diagonal underneath right seat
		seatsAround.append(matrix[row + 1][column + 1])
		# diagonal underneath left seat
		seatsAround.append(matrix[row + 1][column - 1])
	return seatsAround

def traverseMatrix(data, threshold, funName):
	copiedData = deepcopy(data)
	for row in range(0, len(data)):
		for column in range(0, len(data[row])):
			seat = data[row][column]
			neighbors = funName(row, column, data)
			if seat == "L" and "#" not in neighbors: copiedData[row][column] = "#"
			elif seat == "#" and neighbors.count("#") >= threshold: copiedData[row][column] = "L"
	return copiedData

def run(thresHold, funName):
	dOld = deepcopy(data)
	dNew = []
	while True:
		dNew = traverseMatrix(dOld, thresHold, funName)
		if dNew==dOld: 
			return dNew
			break
		else: 
			dOld = deepcopy(dNew)


def count(threshold, funName):
	matrix = run(threshold, funName)
	counter = 0
	for row in matrix:
		counter += row.count("#")
	return counter

"""
------Part 2-------
"""

dimensions = [(-1, 0), (-1, -1), (-1, 1), (1,0), (1,-1), (1, 1), (0, -1), (0, 1)]

def getNeighbors2(row, column, matrix):
		neighbors = []
		for dimension in dimensions:
			newRow = row + dimension[0]
			newColumn = column + dimension[1]
			try:
				while newRow >= 0 and newColumn >= 0:
					newSeat = matrix[newRow][newColumn]
					if newSeat == "L" or newSeat == "#":
						neighbors.append(newSeat)
						break
					newRow += dimension[0]
					newColumn += dimension[1]
			except IndexError:
				pass
		return neighbors

"""
------Solutions-------
"""

print("Part 1: " + str(count(4, getNeighbors)))
print("Part 1: " + str(count(5, getNeighbors2)))