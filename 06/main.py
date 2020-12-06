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
	group = []
	for answer in answers:
		string = ""
		for substr in answer:
			string += substr
		counter += len(set(string))
		group.append([len(answer), string])
	
	print("Part 1: " + str(counter))
	return group

def part2():
	group = part1()
	counter = 0
	for item in group:
		if item[0] == 1: counter += len(item[1])
		else:
			for character in item[1]:
				if item[1].count(character) == item[0]:
					counter += 1
					item[1] = item[1].replace(character, "")
	print(counter)
	
part2()