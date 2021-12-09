#!/usr/bin/env python3
data = [list(map(int, list(line.strip()))) for line in open("input.txt", 'r')]

up = None
down = None
left = None
right = None

mins = []

def get_neighbors(row, col):
	rows = len(data)
	cols = len(data[0]) if rows else 0
	for i in range(max(0, row - 1), min(rows, row + 2)):
		for j in range(max(0, col - 1), min(cols, col + 2)):
			if (i, j) != (row, col):
				yield data[i][j]

mins = []
for row_index, row in enumerate(data):
	for col_index, element in enumerate(row):
		neighbors = list(get_neighbors(row_index, col_index))
		if element < min(neighbors):
			mins.append(element)

mins = [m + 1 for m in mins]
print(sum(mins))