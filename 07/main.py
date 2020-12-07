#!/usr/bin/env python3
file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

items = dict()
for line in data:
	splittedLine = line.replace("bags", "").split(" contain ")
	containedBags = splittedLine[1].split(",")
	items[splittedLine[0].strip()] = containedBags

for key, value in items.items():
	bags = []
	for bag in value:
		if "no other" in bag:
			bags.append(("", 0))
		else: 
			formattedBag = bag.strip().replace(" .", "").replace(".", "").replace("bags", "").replace("bag", "").strip()
			bagTuple = (formattedBag[2:], int(formattedBag[0]))
			bags.append(bagTuple)
	items.update({key: bags})

def getOuterBag(bag):
	bagSet = set()
	for key, value in items.items():
		for v in value:
			if v[0] == bag:
				bagSet.add(key)
	return bagSet

def goThrougSet(bagSet):
	bagSetCopy = bagSet.copy()
	for bag in bagSet:
		newBagSet = getOuterBag(bag)
		bagSetCopy |= newBagSet
		
	bagSetCopy |= bagSet
	
	return bagSetCopy

def part1():
	bagSet = getOuterBag("shiny gold")
	counter = 0
	oldSize = len(bagSet)
	while counter != oldSize:
		oldSize = len(bagSet)
		bagSet |= goThrougSet(bagSet)
		counter = len(bagSet)
	return counter

print("Part 1: " + str(part1()))

def getSubBagsCount(key):
	nestedBags = items[key]
	if nestedBags[0][0] == "":
		return 0
	else:
		counter = 0
		
		for bag in nestedBags:
			counter += bag[1] + bag[1] * getSubBagsCount(bag[0])
			
		return counter

print("Part 2: " + str(getSubBagsCount("shiny gold")))