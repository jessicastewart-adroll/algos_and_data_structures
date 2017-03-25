def rec_forward(matrix):
	height = len(matrix)
	width = len(matrix[0])

	y = 0
	while y < width:
		x = 0
		to_print = []
		while x <= y:
			to_print.append(str(matrix[y-x][x]))	
			x += 1
		print(' '.join(to_print))
		y += 1

	# x = 1
	# while x < size:
	# 	y = size-1
	# 	to_print = []
	# 	j = 1
	# 	while x*j < size:
	# 		to_print.append(str(matrix[y][x*j]))	
	# 		y -= 1
	# 		j += 1
	# 	print(' '.join(to_print))
	# 	x += 1	


# test0 = [[]]
# test1 = [[1]]
# test2 = [
# [1, 2],
# [3, 4],
# [5, 6]]
test3 = [
[1, 2, 3],
[4, 5, 6]]
# test4 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# [10, 11, 12]]

#tests = [test0, test1, test2, test3, test4]
# for test in tests:
rec_forward(test3)
