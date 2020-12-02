#!/usr/bin/env python3
file = "input.txt"

data = [line.strip() for line in open(file, 'r')]

def convertToDicts():
	policies = [dict()]
	for line in data:
		subset = line.split(" ")

		passwordPolicy = {
			"policyTuple": tuple(map(int, subset[0].split("-"))), 
			"letter": subset[1][0],
			"password": subset[2]
		}
		
		policies.append(passwordPolicy)
	return policies

convertedDicts = convertToDicts()

def task1():
	counter = 0
	for value in convertedDicts:
		if bool(value):
			occurences = value["password"].count(value["letter"])
			if value["policyTuple"][0] <= value["password"].count(value["letter"]) <= value["policyTuple"][1]:
				counter += 1
	return counter

def task2():
	counter = 0
	for value in convertedDicts:
		if bool(value):
			validator = False
			first = value["password"][value["policyTuple"][0]-1]
			second = value["password"][value["policyTuple"][1]-1]
			if (first == value["letter"] and second != value["letter"]) \
				or (first != value["letter"] and second == value["letter"]): validator = True
			if validator: counter += 1
	return counter

print("Solution 1: " + str(task1()))
print("Solution 2: " + str(task2()))