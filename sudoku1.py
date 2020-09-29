import json
from seed_sudoku import play
from random import choice

filename = 'sudoku_list/sudoku_list.json'
with open(filename, 'r') as sl:
	sudoku_list = json.load(sl)

play(sudoku_list)