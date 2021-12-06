#!/usr/bin/env python3
data = [int(no) for no in open("input.txt", 'r').read().strip().split(",")]

days = 256
fish = [0] * 9

for t in data:
	fish[t] += 1

for i in range(days):
	spawned = [0] * 9
	for j in range(8):
		spawned[j] = fish[j+1]
	spawned[8] = fish[0]
	spawned[6] += fish[0]
	fish = spawned
	
print(sum(fish))