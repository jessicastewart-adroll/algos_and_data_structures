'''
square maze
start in upper left
end in lower right
possible moves: right, down
0 = wall
1 = path
CREATE SOLUTION MATRIX WITH PATH
'''
def can_move(maze, x, y):
	if x < len(maze) and y < len(maze) and maze[x][y]:
		return True

def solve_maze(maze, x, y, solution):
	if len(maze)-1 == x and len(maze)-1 == y and can_move(maze, x, y):
		solution[y][x] = 1
		return solution

	forward = x+1
	if can_move(maze, forward, y):
		solution[forward][y] = 1
		return solve_maze(maze, forward, y, solution)

	down = y+1
	if can_move(maze, x, down):
		solution[x][down] = 1	
		return solve_maze(maze, x, down, solution)

	return False

def handle_maze(maze):
	size = len(maze)
	solution = [[0]*(size) for i in range(size)]
	if can_move(maze, 0, 0):
		solution[0][0] = 1
	else:
		return False	
	solution = solve_maze(maze, 0, 0, solution)

	if solution:
		for row in solution:
			print(row)
	else:
		print('No solution')		

path_maze = [
[1, 0, 0, 0],
[1, 1, 0, 1],
[0, 1, 0, 0],
[1, 1, 1, 1],
]
no_math_maze = [
[1, 0, 0, 0],
[1, 0, 0, 1],
[0, 1, 0, 0],
[1, 1, 1, 1],
]
# solution = [
# [1, 0, 0, 0],
# [1, 1, 0, 0],
# [0, 1, 0, 0],
# [0, 1, 1, 1],
# ]

tests = [path_maze, no_math_maze]
for test in tests:
	handle_maze(test)
