def print_spiral(matrix):
  left_boundary = 0
  right_boundary = len(matrix[0])
  top_boundary = 0
  bottom_boundary = len(matrix)
  x = 0
  y = 0
  
  while left_boundary <= right_boundary or top_boundary <= bottom_boundary:
    print('to right')
    while x < right_boundary:
      print(matrix[y][x])
      x += 1
    y += 1
    x -= 1
    right_boundary -= 1
    print('to bottom')
    while y < bottom_boundary:
      print(matrix[y][x])
      y += 1
    x -= 1
    y -= 1
    bottom_boundary -= 1
    print('to left')
    while x >= left_boundary:
      print(matrix[y][x])
      x -= 1
    y -= 1
    x += 1
    left_boundary += 1
    print('to top')
    while y >= top_boundary:
      print(matrix[y][x])
      y -= 1
    x += 1
    top_boundary += 1
  
matrix_odd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix_even = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print_spiral(matrix_odd)
