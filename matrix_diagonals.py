'''
[[1, 2],
[3, 4]]
1
3 2
4
'''

def square_forward(matrix):
	size = len(matrix)
	if size != len(matrix[0]): 
		print("Input square")
		return
  
  ## top
	# y = 0
	# while y < size:
	# 	x = 0
	# 	to_print = []
	# 	while x <= y:
	# 		to_print.append(str(matrix[y-x][x]))	
	# 		x += 1
	# 	print(' '.join(to_print))
	# 	y += 1

  ## bottom
	x = 1
	while x < size-1:
		y = size-1
		print(x, y)
		to_print = []
		while x-y > size:
			print(x, y)
			to_print.append(str(matrix[y][x-y]))	
			y -= 1
		print(' '.join(to_print))
		x += 1	


test0 = [[]]
test1 = [[1]]
test2 = [
[1, 2],
[3, 4]]
test3 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

# tests = [test0, test1, test2, test3]
# for test in tests:
# 	
square_forward(test3)
