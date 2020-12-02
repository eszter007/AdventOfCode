#!/usr/bin/env python3
file = "input.txt"

data = [line.strip() for line in open(file, 'r')]

def task1():
	counter = 0
	for line in data:
		subset = line.split(" ")
		times = tuple(map(int, subset[0].split("-")))
		letterToBeContained = subset[1][0]
		password = subset[2]
		occurencesOfLetter = password.count(letterToBeContained)
		if occurencesOfLetter >= times[0] and occurencesOfLetter <= times[1]:
			counter += 1
	print(counter)

def task2():
	counter = 0
	for line in data:
		subset = line.split(" ")
		times = tuple(map(int, subset[0].split("-")))
		letterToBeContained = subset[1][0]
		password = subset[2]
		validator = False
		if password[times[0]-1] == letterToBeContained and password[times[1]-1] != letterToBeContained: validator = True
		elif password[times[0]-1] != letterToBeContained and password[times[1]-1] == letterToBeContained: validator = True
		if validator: counter += 1
	print(counter)

task1()
task2()