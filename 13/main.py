#!/usr/bin/env python3

file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

departure = int(data[0])
busses = data[1].split(",")

def part1():
	busNos = []
	for bus in busses:
		if bus != "x":
			busNos.append(int(bus))
			
	mod = 0
	earliestBus = 0
	for bus in busNos:
		diff = departure % bus
		if (bus - diff) < mod or mod == 0:
			mod = bus - diff
			earliestBus = bus
	print("Part 1: " + str(earliestBus*mod))
part1()