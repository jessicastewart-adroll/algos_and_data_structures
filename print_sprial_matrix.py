def print_spiral(matrix):
  left_boundary = 0
  right_boundary = len(matrix[0])
  top_boundary = 0
  bottom_boundary = len(matrix)
  x = 0
  y = 0
  
  while left_boundary < right_boundary or top_boundary < bottom_boundary:
    level = []
    while x < right_boundary:
      level.append(matrix[y][x])
      x += 1
    y += 1
    x -= 1
    top_boundary += 1
    print(level)
    level = []
    while y < bottom_boundary:
      level.append(matrix[y][x])
      y += 1
    x -= 1
    y -= 1
    right_boundary -= 1
    print(level)
    level = []
    while x >= left_boundary:
      level.append(matrix[y][x])
      x -= 1
    y -= 1
    x += 1
    bottom_boundary -= 1
    print(level)
    level = []
    while y >= top_boundary:
      level.append(matrix[y][x])
      y -= 1
    x += 1
    y += 1
    left_boundary += 1
    print(level)
  
matrix_odd = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix_even = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print_spiral(matrix_even)
