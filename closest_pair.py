import math 

### mergesort
def merge(left_array, right_array, index):
  merged = []
  i = 0
  j = 0
  while i < len(left_array) and j < len(right_array):
    if left_array[i][index] > right_array[j][index]:
      merged.append(right_array[j])
      j += 1
    else:  
      merged.append(left_array[i])
      i += 1
  
  if i < len(left_array):
    merged.extend(left_array[i:])
  if j < len(right_array):
    merged.extend(right_array[j:])  
  return merged  

def merge_sort(array, index=1):
  left = 0
  right = len(array)
  if right <= 1:
    return array
    
  mid = (right-left)//2
  left_array = merge_sort(array[left:mid])
  right_array = merge_sort(array[mid:right])
  return merge(left_array, right_array, index)

def brute_force(pairs):
  min_distance = float('inf')
  i = 0
  while i < len(pairs):
    j = i+1
    while j < len(pairs):
      a = pairs[i]
      b = pairs[j]
      distance = math.sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
      min_distance = min(min_distance, distance)
      j += 1
    i += 1  
  return min_distance

def get_min_distance_y(y_sorted_pairs):
  min_distance = float('inf')
  n = len(y_sorted_pairs)
  i = 0
  while i < n:
    j = i+1
    while j <= i+7 and j < n:
      a = y_sorted_pairs[i]
      b = y_sorted_pairs[j]
      distance = math.sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
      min_distance = min(min_distance, distance)
      j += 1
    i += 1  
  return min_distance

def closest_pair(pairs):
  n = len(pairs)
  if n <= 3:
    return brute_force(pairs)
  
  x_sorted_pairs = sorted(pairs)
  m = n//2
  left = pairs[:m]
  right = pairs[m:]
  ld = closest_pair(left)
  rd = closest_pair(right)
  min_distance = min(ld, rd)

  strip = []
  for point in pairs:
    mid_distance = abs(point[0] - m)
    if mid_distance < min_distance:
      strip.append(point)

  y_sorted_pairs = merge_sort(strip)
  d = get_min_distance_y(y_sorted_pairs)

  return d

  
pairs_test = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]  
print(closest_pair(pairs_test))
print('CORRECT ANSWER', 1.414214)
