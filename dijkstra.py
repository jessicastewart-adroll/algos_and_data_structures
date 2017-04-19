graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
	      [4, 0, 8, 0, 0, 0, 0, 11, 0],
	      [0, 8, 0, 7, 0, 4, 0, 0, 2],
	      [0, 0, 7, 0, 9, 14, 0, 0, 0],
	      [0, 0, 0, 9, 0, 10, 0, 0, 0],
	      [0, 0, 4, 14, 10, 0, 2, 0, 0],
	      [0, 0, 0, 0, 0, 2, 0, 1, 6],
	      [8, 11, 0, 0, 0, 0, 1, 0, 7],
	      [0, 0, 2, 0, 0, 0, 6, 7, 0]]
start = 0  

def min_distance(shortest_distances, finalized):
	min_val = float('-inf')
	min_index = 0

	v = 0
	while v < n-1:
		if finalized[v] == False and shortest_distances[v] <= min_val:
			min_val = shortest_distances[v]
			min_index = v
	v += 1
	return min_index		

def dijkstra(graph, start):
	# all shortest paths
	n = len(graph)
	shortest_distances = [float('inf')]*n
	finalized = [False]*n

	shortest_distances[start] = 0

	i = 0
	while i < n-1:
		shortest = min_distance(shortest_distances, finalized)
		finalized[shortest] = True

		v = 0
		while v < n-1:
			if not finalized[v] \
			and graph[shortest][v] \
			and shortest_distances[shortest] != float('inf')
			and shortest_distances[shortest]+graph[v][shortest] < shortest_distances[v]:
				shortest_distances[v] = shortest_distances[shortest] + graph[shortest][v]
			v+=1
		i+=1
	return shortest_distances

