import sys
from random import randint
import copy

NUM_GENS = 10


def printBoard(board):
	print " ",
	for col in range(1,size-1):
		print col %10,
	print
	for row in range(size-1):
		print row%10,
		for col in range(1, size -1):
			print board[row][col], 
		print

def countNeighbors(board, row, col):
	for i in range(-1,2):
		for j in range(-1,2):
			if (board[row +i][col +j] == "*"):
				neighbors += 1
	return neighbors

def computeNextGen(board):
	nextBoard = copy.deepcopy(board)
	for row in range(1, size-1):
			for col in range(1, size - 1):
				neighbors =countNeighbors(board, row, col)
				if (board[row][col] == "*"):
					if (neighbors < 2 or neighbors >3):
						nextBoard[row][col] = " "
				else:
					if (neighbors == 3):
						nextBoard[row][col] = "*"


board = []
#for i in range(10):
#	board.append(["*"]*10)
for line in sys.stdin:
	size = len(line) - 1
	board.append([])
	for char in line:
		board[len(board) - 1].append(char)

print "Gen 0"
printBoard(board)
for i in range(NUM_GENS):
	print
	print "Gen", (i+1)
	board = computeNextGen(board)
	printBoard(board)
