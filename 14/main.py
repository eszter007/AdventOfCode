#!/usr/bin/env python3
file = "example.txt"
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

print(sequences)