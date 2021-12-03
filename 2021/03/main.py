#!/usr/bin/env python3

#!/usr/bin/env python3
import numpy as np
import statistics

def part1(file):
	data = np.array([list(map(int, list(line.strip()))) for line in open(file, 'r')]).transpose()
	gamma = ""
	epsilon = ""
	
	for line in data:
		counts = np.bincount(line)
		gamma += str(np.argmax(counts))
		epsilon += str(np.argmin(counts))
		
	return int(gamma.encode('ascii'),2) * int(epsilon.encode('ascii'), 2)
	
print(part1("input.txt"))

def calculate(file, isOxygen):
	data = np.array([list(map(int, list(line.strip()))) for line in open(file, 'r')]).transpose()
	binaryString = ""
	i = 0
	while i < np.size(data, 0):
		line = data[i]
		counts = np.bincount(line)
		if len(counts) > 1:
			zeroes = counts[0]
			ones = counts[1]
			currentNo = 0
			if np.size(data, 1) > 1:
				if zeroes != ones:
					if isOxygen:
						currentNo =  np.argmax(counts)
					else:
						currentNo =  np.argmin(counts)
				elif isOxygen:
					currentNo = 1
			elif np.size(data, 1) == 1:
				currentNo = 1
		else: currentNo = 0
		binaryString += str(currentNo)
		
		# remove columns that should be ignored
		indices = []
		for index, no in enumerate(line):
			if no != currentNo:
				indices.append(index)
		data = np.delete(data, indices, axis = 1)
		i += 1
		
	return (binaryString)

def part2(file):
	# run once for Oxygen property and then for CO2 property
	return int(calculate(file, True).encode('ascii'),2) * int(calculate(file, False).encode('ascii'), 2)

print(part2("input.txt"))