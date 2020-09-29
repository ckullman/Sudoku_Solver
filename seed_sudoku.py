from random import choice, sample, randint

def play(list):
	"""Chooses sudoku boards from a list of known solvable boards"""
	board = choice(list)
	sudoku_operations(board)
	print_board(board)
	print("")
	print("_______________________")
	solve(board)
	print_board(board)
	return board 

def sudoku_operations(board):
	"""Chooses a board and modifies it to be different"""
	ops = [randint(0,4), randint(0,4), randint(0,4), randint(0,4)]

	for op in ops:
		if op == 0:
			continue
		if op == 1:
			row_swap3x3(board)
		if op == 2:
			row_swap_internal(board)
		if op == 3:
			column_swap_3x3(board)
		if op == 4:
			column_swap_internal(board)


def row_swap3x3(board):
	"""Swaps 3 rows of the sudoku board with another 3 rows"""
	first = board[:3]
	second = board[3:6]
	third = board[6:]
	new_board = []
	value = 0
	rows = [first, second, third]

	while value < 3:
		a = choice(rows)
		rows.remove(a)
		for i  in range(len(first)):
			new_board.append(a[i])
		value += 1

	return new_board

def row_swap_internal(board):
	"""Swaps rows within the set of 3"""
	first = board[:3]
	second = board[3:6]
	third = board[6:]

	first1 = sample(first, len(first))
	second2 = sample(second, len(second))
	third3 = sample(third, len(third))
	rows = [first1, second2, third3]
	new_board = []

	for i in range(len(rows)):
		for j in range(len(first1)):
			new_board.append(rows[i][j])

	return new_board

def column_swap_3x3(board):
	"""Swaps 3 columns of a board with another 3 columns"""
	column1, column2, column3 = [], [], []
	for i in range(len(board)):
		column1.append(board[i][:3])
		column2.append(board[i][3:6])
		column3.append(board[i][6:])

	columns = [column1, column2, column3]
	shuffeld_columns = sample(columns, len(columns))
	new_board = [[],[],[],[],[],[],[],[],[]]

	for q in range(len(board)):
		for v in range(len(columns)):
			new_board[q].append(shuffeld_columns[0][q][v])

	for w in range(len(board)):
		for e in range(len(columns)):
			new_board[w].append(shuffeld_columns[1][w][e])

	for r in range(len(board)):
		for t in range(len(columns)):
			new_board[r].append(shuffeld_columns[2][r][t])

	return new_board

def column_swap_internal(board):
	"""Swaps columns within the set of three"""
	c1, c2, c3, c4, c5, c6, c7, c8, c9 = [], [], [], [], [], [], [], [], []
	for i in range(len(board)):
		c1.append(board[i][0])
		c2.append(board[i][1])
		c3.append(board[i][2])
		c4.append(board[i][3])
		c5.append(board[i][4])
		c6.append(board[i][5])
		c7.append(board[i][6])
		c8.append(board[i][7])
		c9.append(board[i][8])

	column_group1 = [c1, c2, c3]
	column_group2 = [c4, c5, c6]
	column_group3 = [c7, c8, c8]
	new_board = [[],[],[],[],[],[],[],[],[]]

	cg1_shuffle = sample(column_group1, len(column_group1))
	cg2_shuffle = sample(column_group2, len(column_group2))
	cg3_shuffle = sample(column_group3, len(column_group3))

	for q in range(len(board)):
		new_board[q].append(cg1_shuffle[0][q])

	for w in range(len(board)):
		new_board[w].append(cg1_shuffle[1][w])

	for e in range(len(board)):
		new_board[e].append(cg1_shuffle[2][e])

	for r in range(len(board)):
		new_board[r].append(cg2_shuffle[0][r])

	for t in range(len(board)):
		new_board[t].append(cg2_shuffle[1][t])

	for y in range(len(board)):
		new_board[y].append(cg2_shuffle[2][y])

	for u in range(len(board)):
		new_board[u].append(cg3_shuffle[0][u])

	for p in range(len(board)):
		new_board[p].append(cg3_shuffle[1][p])

	for a in range(len(board)):
		new_board[a].append(cg3_shuffle[2][a])

	return new_board

#Solve board functions
def solve(board):
    """Solves board recursively. Base case of recursion, when no empty spaces can be found. Then we see if numbers 1-9
    will work in a particular spot. If the selected number does work, then the we try to solve the board with the new number.
    If we then cannot solve the board then the the number in the selected position gets appended to zero (empty) and we begin backtracing."""
    find = find_empty(board)
    if not find:
    	return True
    else:
    	row, col = find
    for i in range(1,10):
    	if valid(board, i, (row, col)):
    		board[row][col] = i 

    		if solve(board):
    			return True

    		board[row][col] = 0
    return False

def valid(board, number, position):
	"""Checks whether a number in a position on the board is a valid 'move'"""

	#check row
	for i in range(len(board[0])):
		if board[position[0]][i] == number and position[1] != i:
			return False
	#check column
	for i in range(len(board)):
		if (board[i][position[1]] == number) and position[0] != i:
			return False
	#check box
	box_x = position[1] // 3
	box_y = position[0] // 3 
	for i in range(box_y * 3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if board[i][j] == number and (i,j) != position:
				return False
	return True

def print_board(board):
	"""Function that prints a more readable version of the sudoku board."""
	for i in range(len(board)):

		if i % 3 == 0 and i != 0:
			print("--------------------")

		for j in range(len(board[0])):

			if j % 3 == 0 and j != 0:
				print("|", end = '')

			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ", end="")

def find_empty(board):
	"""Finds the first or next empty space in the board"""
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == 0:
				return (i, j) #returns the row, col
	return None



