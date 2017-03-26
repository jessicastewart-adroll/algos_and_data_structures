def square_backward(matrix):
	size = len(matrix[0])

	x = 0
	while x < size:
		y = 0
		diagonal = []
		while y <= x:
			diagonal.append(str(matrix[y][x-y]))
			y+=1
		print(' '.join(diagonal))
		x+=1

	y = 1
	while y < size:
		x = size-1
		diagonal = []
		col_count = 1
		while y*col_count < size:
			diagonal.append(str(matrix[y*col_count][x]))
			x-=1
			col_count += 1
		print(' '.join(diagonal))
		y+=1	


test0 = [[]]
test1 = [[1]]
test2 = [
[1, 2],
[3, 4]]
test3 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

tests = [test0, test1, test2, test3]
for test in tests:
	square_backward(test)
	print('\n')
