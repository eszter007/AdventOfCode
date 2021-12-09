#!/usr/bin/env python3
data = [int(no) for no in open("input.txt", 'r').read().strip().split(",")]

minimum = min(data)
maximum = max(data)

def triangleFormula(x):
	if x == 0:
		return 0
	else:
		return x * (x+1)/2

def getCost(isPart2):
	latestCost = 99999999999999999999
	for i in range(minimum, maximum + 1):
		cost = 0
		bestPos = 0
		for crab in data:
			if i < crab:
				biggerValue = crab
				smallerValue = i
			else: 
				biggerValue = i
				smallerValue = crab
			difference = biggerValue - smallerValue
			
			if isPart2:
				cost += triangleFormula(difference)
			else:
				cost += difference
			
		if cost < latestCost:
			latestCost = cost
	
	return latestCost

print("Task 1: " + str(int(getCost(False))))
print("Task 2: " + str(int(getCost(True))))