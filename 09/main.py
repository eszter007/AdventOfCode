#!/usr/bin/env python3
import itertools
file = "input.txt"

data = [int(line) for line in open(file, 'r')]

def checkForLength(preambleLength):
	for i in range(0, len(data)):
		arrayToBeChecked = data[i-preambleLength:i]
		found = False
		if len(arrayToBeChecked) == preambleLength:
			for numbers in itertools.combinations(arrayToBeChecked, 2):
				if sum(numbers) == data[i]:
					found = True
					break
			if not found: return data[i]
		i += 1

invalidNumber = checkForLength(25)

print("Part 1: " + str(invalidNumber))

def getWeakness():
	end = 1
	for i in range(0, len(data)):
		value = (0,0)
		while (sum(data[i:end]) <= invalidNumber):
			end += 1
			if (sum(data[i:end]) == invalidNumber) and len(data[i:end]) > 1:
				return min(data[i:end]) + max(data[i:end])
				break
		end = 0

print("Part 1: " + str(getWeakness()))