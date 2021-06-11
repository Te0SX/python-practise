import random

def new_game(n):
	grid = []
	for i in range(n):
		grid.append([0] * n)

	grid = add_two(grid)
	grid = add_two(grid)
	return grid


def add_two(grid):
	a = random.randint(0, len(grid)-1)
	b = random.randint(0, len(grid)-1)
	while grid[a][b] != 0:
		a = random.randint(0, len(grid) - 1)
		b = random.randint(0, len(grid) - 1)
	grid[a][b] = 2
	return grid

def game_state(grid):
	#check for winning cell
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 2048:
				return 'win'
	#check for any zero entries
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				return 'not over'
	#check for same cells that tuch each other
	for i in range(len(grid)-1):
		for j in range(len(grid[0])-1):
			if grid[i][j] == grid[i+1][j] or grid[i][j+1] == grid[i][j]:
				return 'not over'
	# to check the left/right entries on the last row
	for k in range(len(grid)-1):
		if grid[len(grid)-1][k] == grid[len(grid)-1][k+1]:
			return 'not over'
	# check up/down entries on last column
	for l in range(len(grid)-1):
		if grid[l][len(grid)-1] == grid[l+1][len(grid)-1]:
			return 'not over'
	return 'lose'

	