#!/usr/bin/env python3
from copy import deepcopy
file = "input.txt"
data = [line for line in open(file, 'r')]

#
# Formatting the data
#
answers = [[]]
i = 0
for line in data:
	line = line.strip()
	if line[:4] == "mask":
		i += 1
		answers.append([])
	answers[i].append(line.split(","))

sequences = []
for line in answers:
	valuePairs = []
	for value in line:
		valuePair = tuple()
		value = value[0].split(" = ")
		if "[" in value[0]:
			value[0] = value[0].split("[")[1].split("]")[0]
		if value[0] == "mask":
			valuePair = value[0], value[1]
		else: 
			valuePair = int(value[0]), int(value[1])
		valuePairs.append(valuePair)
	if len(line) != 0:
		sequences.append(valuePairs)

#
# Helper functions
#

def getBinaryNumber(decimal):
	res = [int(i) for i in list('{0:0b}'.format(decimal))]
	
	counter = len(res)
	while counter < 36:
		res.insert(0, 0)
		counter += 1
	return res

def binaryToDecimal(binaryNumber):
	return int("".join(str(x) for x in binaryNumber), 2) 

#
# Part 1
#

def applyMaskNoFloating(mask, binaryNumber):
	newBinary = []
	for i in range(0, len(mask)):
		if mask[i] == "X":
			newBinary.append(binaryNumber[i])
		elif mask[i] == "1" and binaryNumber[i] == 1:
			newBinary.append(1)
		elif mask[i] == "1" and binaryNumber[i] == 0:
			newBinary.append(1)
		elif mask[i] == "0" and binaryNumber[i] == 1:
			newBinary.append(0)
		elif mask[i] == "0" and binaryNumber[i] == 0:
			newBinary.append(0)
	return newBinary

def part1():
	memory = dict()
	for sequence in sequences:
		mask = sequence[0][1]
		values = sequence[1:]
		for value in values:
			memory[value[0]] = binaryToDecimal(applyMaskNoFloating(mask, getBinaryNumber(value[1])))
	
	print("Part 1: " + str(sum(memory.values())))

part1()

#
# Part 2
#

def applyFloatingMask(mask, binaryNumber):
	newBinary = []
	for i in range(0, len(mask)):
		if mask[i] == "X":
			newBinary.append(("X"))
		elif mask[i] == "0":
			newBinary.append(binaryNumber[i])
		elif mask[i] == "1":
			newBinary.append(1)
	return newBinary

# get the possibilites once
def getPossibilities(floatingValue):
	poss = []
	for i in range(0, len(floatingValue)):
		b1 = deepcopy(floatingValue)
		b2 = deepcopy(floatingValue)
		if floatingValue[i] == "X":
			b1[i] = 1
			poss.append(b1)
			b2[i] = 0
			poss.append(b2)
			break
	return poss


def loopPossibilites(mask, binaryNumber):
	poss = getPossibilities(applyFloatingMask(mask, binaryNumber))
	
	while len(poss) != 0:
		pa = []
		for p in poss:
			p = getPossibilities(p)
			pa += p
		if len(pa) != 0:
			poss = pa
		else: break
	return poss

def getDecimals(mask, binaryNumber):
	decimals = []
	possibilities = loopPossibilites(mask, binaryNumber)
	for p in possibilities:
		decimals.append(binaryToDecimal(p))
	return decimals

def part2():
	memory = dict()
	for sequence in sequences:
		mask = sequence[0][1]
		values = sequence[1:]
		for value in values:
			decs = getDecimals(mask, getBinaryNumber(value[0]))
			for d in decs:
				memory[d] = value[1]
	print("Part 2: " + str(sum(memory.values())))

part2()