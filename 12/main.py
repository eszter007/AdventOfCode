file = "input.txt"
data = [line.strip() for line in open(file, 'r')]

directions = []
for d in data:
	tup = (d[0], int(d[1:]))
	directions.append(tup)

eastCounter = 0
northCounter = 0
north = False
east = True
south = False
west = False
for direction in directions:
	if direction[0] == "N":
		northCounter += direction[1]
	elif direction[0] == "S":
		northCounter -= direction[1]
	elif direction[0] == "E":
		eastCounter += direction[1]
	elif direction[0] == "W":
		eastCounter -= direction[1]
	elif direction[0] == "R":
		moveTimes = direction[1]/90
		while moveTimes != 0:
			if north:
				north = False
				east = True
				south = False
				west = False
			elif east:
				north = False
				east = False
				south = True
				west = False
			elif south:
				north = False
				east = False
				south = False
				west = True
			elif west:
				north = True
				east = False
				south = False
				west = False
			moveTimes -= 1
	elif direction[0] == "L":
		moveTimes = direction[1]/90
		while moveTimes != 0:
			if north:
				north = False
				east = False
				south = False
				west = True
			elif east:
				north = True
				east = False
				south = False
				west = False
			elif south:
				north = False
				east = True
				south = False
				west = False
			elif west:
				north = False
				east = False
				south = True
				west = False
			moveTimes -= 1
	elif direction[0] == "F":
		if north:
			northCounter += direction[1]
		elif south:
			northCounter -= direction[1]
		elif east:
			eastCounter += direction[1]
		elif west:
			eastCounter -= direction[1]

print(abs(northCounter) + abs(eastCounter))