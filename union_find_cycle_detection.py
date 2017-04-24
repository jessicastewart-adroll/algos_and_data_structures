### naive 
graph_one = {
	0: [1, 2],
	1: [0, 2],
	2: [1, 0]
}

graph_two = {
	0: [1],
	1: []
}

def union(parents, vertex_one, vertex_two):
	subset_one = find_parent(parents, vertex_one)
	subset_two = find_parent(parents, vertex_two)
	parents[subset_one] = subset_two

def find_parent(parents, vertex):
	if parents[vertex] == -1:
		return vertex
	else:
		# traverse up for parent
		return find_parent(parents, parents[vertex])	

def detect_cycle(graph):
	verticies = len(graph.keys())
	parents = [-1]*verticies

	for vertex in graph:
		for neighbor in graph[vertex]:
			a = find_parent(parents, vertex)
			b = find_parent(parents, neighbor)
			if a == b:
				return True
			union(parents, a, b)	
	return False		

print(detect_cycle(graph_one))	
print(detect_cycle(graph_two))		

### rank
graph_one = {
	0: [1, 2],
	1: [0, 2],
	2: [1, 0]
}

graph_two = {
	0: [1],
	1: []
}

def make_parents(vertex_count):
	return [(-1, 0)]*vertex_count

def find_parent(parents, x):
	if parents[x][0] == -1:
		return x
	else:
		return find_parent(parents[x])	

def union(parents, x, y):
	x_subset = find_parent(parents, x)
	y_subset = find_parent(parents, y)

	if x_subset == y_subset:
		return

	if x_subset[1] < y_subset[1]:
		x_subset[0] = y_subset
	elif x_subset[1] > y_subset[1]:
		y_subset[0] = x_subset
	else:
		y_subset[0] = x_subset
		x_subset[1] += 1	

def detect_cycle(graph):
	verticies = len(graph.keys())
	parents = make_parents(vertices)

	for vertex in graph:
		for neighbor in graph[vertex]:
			a = find_parent(parents, vertex)
			b = find_parent(parents, neighbor)
			if a[0] == b[0]:
				return True
			union(parents, a, b)	
	return False		

print(detect_cycle(graph_one))	
print(detect_cycle(graph_two))			
