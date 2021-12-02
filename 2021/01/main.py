#!/usr/bin/env python3
import re

data = [int(line.strip()) for line in open("input_1.txt", 'r')]

def calculateSubmarine(data):
	counter = 0
	previousNumber = 0
	for number in data:
		if (previousNumber != 0) and number > previousNumber:
			counter +=1
		previousNumber = number
	return counter


print("Task 1: " + str(calculateSubmarine(data)))

def calculateSlidingSums(data):
	list = []
	for index, line in enumerate(data):
		if index + 2 < len(data):
			list.append(line + data[index+1] + data[index+2])
	return list

print("Task 2: " + str(calculateSubmarine(calculateSlidingSums(data))))