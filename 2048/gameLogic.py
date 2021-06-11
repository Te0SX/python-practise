import random
import colorPalette as c

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
		# intentionally reduced to check the row on the right and below
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

def reverse(grid):
    new_grid = []
    for i in range(len(grid)):
        new_grid.append([])
        for j in range(len(grid[0])):
            new_grid[i].append(grid[i][len(grid[0])-j-1])
    return new_grid

def transpose(grid):
	new_grid = []
	for i in range(len(grid[0])):
		new_grid.append([])
		for j in range(len(grid)):
			new_grid[i].append(grid[j][i])
	return new_grid


# The way to do movement is compress -> merge -> compress again

def cover_up(grid):
	new_grid = []
	for j in range(c.GRID_LEN):
		partial_new_grid = []
		for i in range(c.GRID_LEN):
			partial_new_grid.append(0)
		new_grid.append(partial_new_grid)
	done = False
	for i in range(c.GRID_LEN):
		count = 0
		for j in range(c.GRID_LEN):
			if grid[i][j] != 0:
				new_grid[i][count] = grid[i][j]
				if j != count:
					done = True
				count += 1
	return new_grid, done


def merge(grid, done):
	for i in range(c.GRID_LEN):
		for j in range(c.GRID_LEN-1):
			if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
				grid[i][j] *= 2
				grid[i][j+1] = 0
				done = True
	return grid, done


def up(game):
	print("up")
	# return grid after shifting up
	game = transpose(game)
	game, done = cover_up(game)
	game, done = merge(game, done)
	game = cover_up(game)[0]
	game = transpose(game)
	return game, done


def down(game):
	print("down")
	# return grid after shifting down
	game = reverse(transpose(game))
	game, done = cover_up(game)
	game, done = merge(game, done)
	game = cover_up(game)[0]
	game = transpose(reverse(game))
	return game, done


def right(game):
	print("down")
	# return matrix after shifting right
	game = reverse(game)
	game, done = cover_up(game)
	game, done = merge(game, done)
	game = cover_up(game)[0]
	game = reverse(game)
	return game, done


def left(game):
    print("left")
    # return matrix after shifting left
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done
	

	