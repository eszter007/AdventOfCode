#!/usr/bin/env python3
import re

file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

#
# Part 1
#

def run(calc):
	match = re.search(r'\(([0-9]|\*|\+|\s)*\)', calc)
	if match:
		subExpression = match.group()[1:-1].strip()
		subRange = match.span()
		before = calc[0:subRange[0]]
		after = calc[subRange[1]:]
		return run(before + str(calculate(subExpression)) + after)
	return calculate(calc)

def calculate(calc):
	calc = calc.split()
	num = 0
	symbol = ""
	for i, char in enumerate(calc):
		if i == 0:
			num = char
		elif char in ["*", "+"]:
			symbol = char
		else:
			num = eval(str(num) + symbol + char)
	return num

def part1():
	solutions = []
	for line in data:
		solutions.append(run(line))
	
	print("Part 1: " + str(sum(solutions)))

part1()