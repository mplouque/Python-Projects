def solve(size):
	createBoard(size)
	#put down first queen
	#inserts on this board at 0,0
	
	insertQueen(board, 0,0)





def createBoard(size):
	board = [[ "*" for x in range(size)] for x in range(size)]
	print board
createBoard(5)

#r and c represent the current row and column beginning with zero
def insertQueen(board, currentR, currentC):
	#places a queen at the end if it makes it there
	#if your next move would place a queen to the right of the board print the board.
	if (currentR > len(board) -1):
		return board
	#checks every column
	while (currentC , len(board):
		# if it is safe then place a queen
	
	
	
'''
board = []
for c in range(0, len(ls)):
	board.append(ls)
print board
def checkIfDone(board):
	if ("*" in board):
		print "You arent done"
		return 
	else:
		print "No more possible moves"
		return 
checkIfDone(board)
'''
