def rec_backward(matrix):
	width = len(matrix[0])
	height = len(matrix)

	x = 0
	while x < width:
		y = 0
		diagonal = []
		while y <= x and y < height:
			diagonal.append(str(matrix[y][x-y]))
			y+=1
		print(' '.join(diagonal))
		x+=1

	y = 1
	while y < height:
		x = width-1
		diagonal = []
		col_count = 1
		while y*col_count < height and x >= 0:
			diagonal.append(str(matrix[y*col_count][x]))
			x-=1
			col_count += 1
		print(' '.join(diagonal))
		y+=1	


test0 = [[]]
test1 = [[1]]
test2 = [
[1, 2, 3],
[3, 4, 6]]
test3 = [
[1, 2],
[3, 4],
[5, 6]]
test4 = [
[1],
[2],
[3],
[4]]

tests = [test0, test1, test2, test3, test4]
for test in tests:
	rec_backward(test)
	print('\n')
