'''
GIVEN: MxN
[[9 3 2]
[8 6 1]
[5 5 6]
[1 2 8]]

OUTPUT:
9      
3 8 
2 6 5  
1 5 1 
6 2  
8  

  00
  01 10
  02 11 20
  12 21 30
  22 31 
  23
'''
def print_backwards_diagonals(matrix):
  m = len(matrix)
  n = len(matrix[0])
  
  output_rows = m + n - 1
  
  for row in range(0, output_rows):
    out = 0
    while out < n:
      i = 0
      j = 0
    print(row)
    matrix[i][j]
    j += 1
    
test = [[9, 3, 2],
[8, 6, 1],
[5, 5, 6],
[1, 2, 8]]
print_backwards_diagonals(test) 
