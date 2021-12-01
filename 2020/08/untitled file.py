#!/usr/bin/env python3

def part2():
	for i in range(0, len(data)):
		dataCopy = data
		if dataCopy[i][0] == nop:
			dataCopy[i][0] = jmp
		elif dataCopy[i][0] == jmp: 
			dataCopy[i][0] = nop
			#print(dataCopy)
part2()