#!/usr/bin/env python3
file = "input.txt"
data = sorted([int(line) for line in open(file, 'r')])

def part1():
	oneCounter = 0
	threeCounter = 1
	for i in range(0, len(data)):
		if i > 0 and i < len(data)-1:
			difference = data[i+1] - data[i]
		elif i == 0: difference = data[i]
		else: difference = data[i] - data[i-1]
		if difference == 1:
			oneCounter += 1
		elif difference == 3:
			threeCounter += 1
	print("Part 1: " + str(threeCounter*oneCounter))

"""
Approach:
- Split sorted array into subarrays 
- Solve problems indenpendently (max length = 5)
- Multiply the results
"""
	
def evaluate(value):
	length = len(value)
	if length == 4: numberOfCombinations = 4
	if length == 5: numberOfCombinations = 7
	if length == 3: numberOfCombinations = 2
	if length <= 2: numberOfCombinations = 1
	return numberOfCombinations

def part2():
	# add start and end value to array
	data.insert(0, 0)
	data.append(max(data)+3)
	
	subarrays = [[]]
	i = 0
	j = 0
	multipliedValue = 1
	
	for i in range(0, len(data)):
		if len(subarrays) <= j: 
			subarrays.append([])
			subarrays[j].append(data[i])
		else:
			difference = 0
			if len(subarrays[j]) > 0: 
				difference = data[i] - subarrays[j][-1]
			if difference == 3:
				j += 1
				subarrays.append([])
				subarrays[j].append(data[i])
				multipliedValue *= evaluate(subarrays[j-1])
			else: 
				subarrays[j].append(data[i])
				
	print("Part 2: " + str(multipliedValue))

part1()
part2()