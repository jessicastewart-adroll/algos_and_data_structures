'''
1. handle initial case
2. handle no solution
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

maze = [
[1, 0, 0, 0],
[1, 1, 0, 1],
[0, 1, 0, 0],
[1, 1, 1, 1],
]
size = len(maze)
solution = [[0]*(size) for i in range(size)]
solution = solve_maze(maze, 0, 0, solution)

for row in solution:
	print(row)
# solution = [
# [1, 0, 0, 0],
# [1, 1, 0, 0],
# [0, 1, 0, 0],
# [0, 1, 1, 1],
# ]
