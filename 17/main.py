#!/usr/bin/env python3

file = "example.txt"
data = [line.strip() for line in open(file, 'r')]
print(data)

ACTIVE = "#"
INACTIVE = "."

z0 = []
for line in data:
	l = []
	for c in line:
		l.append(c)
	z0.append(l)

print(z0)
z1 = []
z