from collections import defaultdict
from math import sqrt

def closest_pair(pairs):
  min_distance = float('inf')
  i = 0
  j = 0 
  while i < len(pairs):
    a = pairs[i]
    j = i+1
    while j < len(pairs):
      b = pairs[j]
      distance = sqrt(pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2))
      min_distance = min(min_distance, distance)
      j+=1
    i+=1

  return min_distance
  
pairs_test = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]  
print(closest_pair(pairs_test))
