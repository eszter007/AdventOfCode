#!/usr/bin/env python3

# understood the task 2 wrong
# keeping this if I need it later
def createSums(file):
	items = dict()
	data = [list(filter(None, re.split('(\d+)', line.replace(" ", "").strip()))) for line in open(file, 'r')]
	for number, letters in data:
		for letter in letters:
			if letter in items: 
				items[letter] += int(number)
			else:
				items[letter] = int(number)
	return items

def part2(file):
	data = list(createSums(file).values())
	return (calculateSubmarine())

print(part2("example_input_2.txt"))