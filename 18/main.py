#!/usr/bin/env python3
import re

file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

#
# Part 1
#

def run(calc, name):
	match = re.search(r'\(([0-9]|\*|\+|\s)*\)', calc)
	if match:
		subExpression = match.group()[1:-1].strip()
		subRange = match.span()
		before = calc[0:subRange[0]]
		after = calc[subRange[1]:]
		return run(before + str(name(subExpression)) + after, name)
	return name(calc)

def calculate(calc):
	calc = calc.split()
	num = 0
	symbol = ""
	for i, char in enumerate(calc):
		if i == 0: num = char
		elif char in ["*", "+"]: symbol = char
		else: num = eval(str(num) + symbol + char)
	return num

def parts(name):
	solutions = []
	for line in data:
		solutions.append(run(line, name))
	return str(sum(solutions))

#
# Part 2
#

def calcAddition(calc):
	match = re.search(r'[0-9]+\s\+\s[0-9]+', calc)
	if match:
		subExpression = match.group()
		subRange = match.span()
		before = calc[0:subRange[0]]
		after = calc[subRange[1]:]
		return calcAddition(before + str(eval(subExpression)) + after)
	else: return eval(calc)

#
# Solutions
#

print("Part 1: " + parts(calculate))
print("Part 2: " + parts(calcAddition))