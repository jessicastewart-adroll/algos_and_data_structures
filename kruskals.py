graph = [
[0, 3, 1, 8, 9],
[3, 0, 5, 7, 6],
[1, 5, 0, 1, 2],
[8, 7, 1, 0, 3],
[9, 6, 2, 3, 0]
]

from heapq import *

def find(subsets, a, b):
	return subsets[a] == subsets[b]

def union(subsets, a, b):
	later = max(a, b)
	earlier = min(a, b)
	i = 0
	while i < len(subsets):
		if subsets[i] == later:
			subsets[i] = earlier
		i+=1

def kruskals(graph):
	n = len(graph)
	edges = []
	for i in range(n-1):
		for j in range(i+1, n):
			if graph[i][j]:
				heappush(edges, (graph[i][j], i, j))

	subsets = [i for i in range(n)]			

	mst = []
	while len(mst) < n-1:
		edge = heappop(edges)
		if not find(subsets, edge[1], edge[2]):
			mst.append(edge)
			union(subsets, edge[1], edge[2])

	return mst
	
print(kruskals(graph))		
