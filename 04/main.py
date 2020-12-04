#!/usr/bin/env python3
import re

def convertToDicts(file):
	data = [line for line in open(file, 'r')]
	
	passports = [[]]
	i = 0
	for line in data:
		if line == "\n":
			i += 1
			passports.append([])
			continue
		passports[i].append(line.strip())
					
	batch = []
	for passport in passports:
		entries= dict()
		for line in passport:
			entries.update(dict((x.strip(), y.strip()) 
						for x, y in (element.split(':')  
						for element in line.split(' '))))
		batch.append(entries)
	return batch

passports = convertToDicts("input.txt")

def task1():
	counter = 0
	validPassports = []
	for passport in passports:
		if len(passport) == 8:
			counter += 1
			validPassports.append(passport)
		elif len(passport) == 7 and (not ('cid' in passport)):
			counter += 1
			validPassports.append(passport)
	print("Part 1: " + str(counter))
	return validPassports
	
def task2():
	validPassports = task1()
	counter = 0
	for passport in validPassports:
		if birthYear(passport) and issueYear(passport) and expirationDate(passport) \
		and hairColor(passport) and eyeColor(passport) and passPortID(passport):
			unit = passport['hgt'][-2:]
			try:
				height = int(passport['hgt'][:-2])
			except:
				continue
			if unitCheck(height, unit):
					counter += 1
	print("Task 2: " + str(counter))
						

def birthYear(passport):
	if (1920 <= int(passport['byr']) <= 2002):
		return True
	return False

def issueYear(passport):
	if 	(2010 <= int(passport['iyr']) <= 2020):
		return True
	return False

def expirationDate(passport):
	if (2020 <= int(passport['eyr']) <= 2030):
		return True
	return False

def unitCheck(height, unit):
	if ((unit == "cm") and (150 <= height <= 193)) or \
		((unit == "in") and (59 <= height <= 76)):
		return True
	return False

def hairColor(passport):
	if (passport['hcl'][0] == "#"):
		color = passport['hcl'][1:]
		if (len(color) == 6) and re.match(".*[0-9a-f].*", color):
			return True
	return False

def eyeColor(passport):
	eyeColor = passport["ecl"]
	if (eyeColor == "amb") or (eyeColor == "blu") \
	or (eyeColor == "brn") or (eyeColor == "gry") \
	or (eyeColor == "grn") or (eyeColor == "hzl") or (eyeColor == "oth"):
		return True
	return False

def passPortID(passport):
	passPortID = passport["pid"]
	if (len(passPortID) == 9) and re.match(".*[0-9].*", passPortID):
		return True
	return False

task2()