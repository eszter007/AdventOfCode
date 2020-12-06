#!/usr/bin/env python3
file = "input.txt"

data = [line for line in open(file, 'r')]

answers = [[]]
i = 0
for line in data:
	if line == "\n":
		i += 1
		answers.append([])
		continue
	answers[i].append(line.strip())

def part1():
	counter = 0
	for answer in answers:
		string = ""
		for substr in answer:
			string += substr
		counter += len(set(string))
	
	print("Part 1: " + str(counter))

part1()


	