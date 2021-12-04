#!/usr/bin/env python3

data = [line.strip().split("\n\n") for line in open("input.txt", 'r')]
drawed = list(map(int, data[0][0].split(",")))
data.pop(0)
boards = list()
currentBoard = []
for entry in data:
	if entry[0]:
		line = list(map(int, entry[0].split()))
		currentBoard.append(line)
	elif currentBoard:
		boards.append(currentBoard)
		currentBoard = []
boards.append(currentBoard)

def isHorizontalBingo(board, drawed):
	for line in board:
		if set(line).issubset(set(drawed)):
			return True
		
def isVerticalBingo(board, drawed):
	# inverse the matrix
	newBoard = list(zip(*board))
	return isHorizontalBingo(newBoard, drawed)

def isBingo(board, drawed):
	if isHorizontalBingo(board, drawed) or isVerticalBingo(board, drawed):
		return True
	else: 
		return False

# Task 1
def playBingo():
	currentlyDrawed = []
	index = 0
	wonBingo = False
	winner = list()
	calledNumber = 0
	while index < len(drawed) and not wonBingo:
		currentlyDrawed.append(drawed[index])
		for board in boards:
			if isBingo(board, currentlyDrawed):
				winner = [x for sublist in board for x in sublist]
				wonBingo = True
				calledNumber = drawed[index]
				break
		if not wonBingo:
			index += 1
			
	if wonBingo:
		otherNumbers = [i for i in winner if i not in currentlyDrawed]
		print(sum(otherNumbers)*calledNumber)

playBingo()

# Task 2
def playBingo2():
	currentlyDrawed = []
	index = 0
	wonBingo = False
	winner = list()
	calledNumber = 0
	checkedBoards = []
	while index < len(drawed) and not wonBingo:
		currentlyDrawed.append(drawed[index])
		for board in boards:
			if isBingo(board, currentlyDrawed):
				if not board in checkedBoards:
					checkedBoards.append(board)
				if len(checkedBoards) == len(boards):
					winner = [x for sublist in board for x in sublist]
					wonBingo = True
					calledNumber = drawed[index]
					break
		index += 1
			
	if wonBingo:
		otherNumbers = [i for i in winner if i not in currentlyDrawed]
		print(str(sum(otherNumbers)*calledNumber))
		
playBingo2()
