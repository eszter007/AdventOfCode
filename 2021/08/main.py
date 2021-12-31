#!/usr/bin/env python3

data = [l.split(" | ") for l in (line.strip() for line in open("input.txt", 'r'))]

for i, line in enumerate(data):
	for j, entry in enumerate(line):
		entry = entry.split(" ")
		data[i][j] = entry

def part1():
	counter = 0
	for line in data:
		toBeChecked = line[1]
		for char in toBeChecked:
			lengthToCheck = len(char)
			if lengthToCheck in [2, 3, 4, 7]:
				counter += 1
			
	print(counter)
	
part1()

def part2():
	sums = []
	for line in data:
		numbers = [None] * 10
		digits = line[0]
		l = []
		while None in numbers:
			for digit in digits:
				digit = list(digit)
				length = len(digit)
				if length == 2:
					numbers[1] = digit
				elif length == 4:
					numbers[4] = digit
				elif length == 3:
					numbers[7] = digit
				elif length == 7:
					numbers[8] = digit
				elif length == 5:
					if numbers[1] != None:
						if set(numbers[1]).issubset(set(digit)):
							numbers[3] = digit
						elif set(l).issubset(set(digit)):
							numbers[5] = digit
						else:
							numbers[2] = digit
				elif length == 6:
					if set(l).issubset(set(digit)):
						if numbers[1] != None:
							if set(numbers[1]).issubset(set(digit)):
								numbers[9] = digit
							else:
								numbers[6] = digit
					else:
						numbers[0] = digit
				if numbers[1] != None and numbers[4] != None :
					interSectionOneFour = list(set(numbers[4]) & set(numbers[1]))
					l = [x for x in numbers[4] if x not in interSectionOneFour]
					
		toBeChecked = line[1]
		numberString = ""
		for group in toBeChecked:
			for i, number in enumerate(numbers):
				if set(number) == set(group):
					numberString  += str(i)
		sums.append(int(numberString))
	return sums

print(sum(part2()))