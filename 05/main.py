#!/usr/bin/env python3
import math
file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

def calculateRow (smallestNo, highestNo, rowRange):
	for character in rowRange:
		if character == "F" or character == "L":
			highestNo = math.floor((highestNo - smallestNo)/2) + smallestNo
		if character == "B" or character == "R":
			smallestNo = highestNo - math.floor((highestNo - smallestNo)/2) 
		if highestNo == smallestNo:
			return smallestNo

def part1():
	numbers = []
	for line in data:
		row = calculateRow(0, 127, line[:7])
		column = calculateRow(0, 7, line[-3:])
		multiply = row * 8 + column
		numbers.append(multiply)
	print("Part 1: " + str(max(numbers)))
	return numbers

def task2():
	numbers = sorted(part1())
	currentNumber = 0
	for number in numbers:
		if number == (currentNumber + 2):
			print("Part 2: " + str(number - 1))
		currentNumber = number

task2()