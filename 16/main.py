#!/usr/bin/env python3
import statistics
file = "input.txt"
data = [line for line in open(file, 'r')]

###
### format notes
###

notes = [[]]
i = 0
for line in data:
	if line == "\n":
		i += 1
		notes.append([])
		continue
	notes[i].append(line.strip())

notes[1].pop(0)
notes[2].pop(0)

def formatTickets(tickets):
	formattedTickets = []
	for ticket in tickets:
		formattedTicket = []
		formattedTicket = [int(t) for t in ticket.split(",")]
		formattedTickets.append(formattedTicket)
	return formattedTickets

notes[1] = formatTickets(notes[1])[0]
notes[2] = formatTickets(notes[2])

# format criteria
criteria = []
for value in notes[0]:
	tup = []
	value = value.split(": ")[1]
	value = value.split(" or ")
	for v in value:
		v = tuple(map(int, v.split('-'))) 
		tup.append(v)
	criteria.append(tup)
notes[0] = criteria

#
# Part 1
#

def ticketFieldValid(number):
	for criteria in notes[0]:
		for c in criteria:
			if number in range(c[0], c[1]+1): return True
	return False

def part1():
	invalidFields = []
	for ticket in notes[2]:
		for number in ticket:
			if not ticketFieldValid(number): 
				invalidFields.append(number)
	print("Part 1: " + str(sum(invalidFields)))

part1()

#
# Part 2
#
# To Do
# Issue: Not all fields are considered
#

for ticket in notes[2]:
	for number in ticket:
		if not ticketFieldValid(number): 
			notes[2].remove(ticket)

def validForRow(number, row):
	for tup in row:
		if number in range(tup[0], tup[1]+1): return True
	return False

checkedFields = {}

for field in notes[0]:
	possibleIndices = []
	for i in range(0, len(notes[1])):
		holds = True
		for ticket in notes[2]:
			if not validForRow(ticket[i], field): holds = False
		if holds: 
			possibleIndices.append(i)
	checkedFields[str(field)] = possibleIndices

for k in checkedFields:
	print(k, checkedFields[k])
