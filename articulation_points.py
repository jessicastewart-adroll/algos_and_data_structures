import copy

def is_connected(graph):
	n = len(graph)
	visited = set()
	queue = [0]

	while queue:
		vertex = queue.pop(0)
		for i, neighbor in enumerate(graph[vertex]):
			if neighbor and i not in visited:
				visited.add(i)
				queue.append(i)
	return len(visited) == n	

def graph_wo_copy(graph, vertex):	
	graph_wo_vertex = copy.deepcopy(graph)
	graph_wo_vertex.pop(vertex)
	for row in graph_wo_vertex:
		row.pop(vertex)			
	return graph_wo_vertex		


def find_articulation_points(graph):
	articulation_points = []
	n = len(graph)
	for vertex in range(n):
		graph_wo_vertex = graph_wo_copy(graph, vertex)

		if not is_connected(graph_wo_vertex):
			articulation_points.append(vertex)

	return articulation_points		

graph_one_matrix = [
	[0, 1, 1, 1, 0],
	[1, 0, 1, 0, 0],
	[1, 1, 0, 0, 0],
	[1, 0, 0, 0, 1],
	[0, 0, 0, 1, 0],
]	

print(find_articulation_points(graph_one_matrix))
