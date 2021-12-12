#!/usr/bin/env python3
data = [list(map(int, list(line.strip()))) for line in open("input.txt", 'r')]
nones = [ None for i in range(len(data[1])+2) ] 
for line in data:
	line.append(None)
	line.insert(0, None)

data.insert(0, nones)
data.append(nones)

def getNeighbors(row, column):
	up = row - 1
	down = row + 1
	left = column - 1
	right = column + 1
	
	top = {"row": up, "col": column}
	topLeft = {"row": up, "col": left}
	topRight = {"row": up, "col": right}
	bottom = {"row": down, "col": column} 
	bottomLeft = {"row": down, "col": left}
	bottomRight = {"row": down, "col": right}
	leftElement = {"row": row, "col": left}
	rightElement = {"row": row, "col": right}
	
	return top, topLeft, topRight, bottom, bottomLeft, bottomRight, leftElement, rightElement
	
def recurseFlash(element):
	coordinates = [element["row"], element["col"]]
	flashed.append(coordinates)
	if data[element["row"]][element["col"]] != None:
		neighbors = getNeighbors(element["row"], element["col"])
		for neighbor in neighbors:
			if data[neighbor["row"]][neighbor["col"]] != None:
				data[neighbor["row"]][neighbor["col"]] += 1
				isInArray = False
				for c in flashed:
					if c[0] == neighbor["row"] and c[1] == neighbor["col"]: isInArray = True; break
				if not isInArray and data[neighbor["row"]][neighbor["col"]] > 9:
					recurseFlash(neighbor)


def checkIfAllFlashed():
	for line in data:
		for element in line:
			if element != 0 and element != None:
				return False
	return True
	
counter = 0
for step in range(0, 500):
	flashed = []
	
	for rowIndex, line in enumerate(data):
		for colIndex, element in enumerate(line):
			if element != None:
				data[rowIndex][colIndex] += 1
	
	for row_index, row in enumerate(data):
		for col_index, element in enumerate(row):
			if element != None:
				input = {"row": row_index, "col": col_index, "element": element}
				isInArray = False
				for c in flashed:
					if c[0] == row_index and c[1] == col_index: isInArray = True; break
				if not isInArray and element > 9:
					recurseFlash(input)
					
	for row_index, row in enumerate(data):
		for col_index, element in enumerate(row):
			if element != None:
				if element > 9:
					data[row_index][col_index] = 0

	
	counter += len(flashed)
	
	if step == 99:
		print("Part 1: " + str(counter))

	if checkIfAllFlashed():
		print("Part 2: " + str(step+1))
		break