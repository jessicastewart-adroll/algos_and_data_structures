graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
def dfs_all_paths(graph, start, end):
  stack = [(start, [start])]
  paths = []
  
  while stack:
    node, path = stack.pop()
    for adj in graph[node]:
      if adj not in path:
        if adj == end:
          paths.append(path+[adj])
        else:
          stack.append((adj, path+[adj]))
        
  return paths      
  
print(dfs_all_paths(graph, 'A', 'F'))
###
graph = {
			'A': set(['B', 'C']),
			'B': set(['A', 'D', 'E']),
			'C': set(['A', 'F']),
			'D': set(['B']),
			'E': set(['B', 'F']),
			'F': set(['C', 'E'])
		}
		
# dfs of entire graph
# {'E', 'D', 'F', 'A', 'C', 'B'}
def dfs(graph, start):
	stack = [start]
	path = set()

	while stack:
		node = stack.pop()
		if node not in path:
			path.add(node)
			for n in graph[node]:
				if n not in path:
					stack.append(n)

	print('visited', path)


dfs(graph, 'A')

# with array ['A', 'B', 'E', 'F', 'C', 'D']
# with set {'C', 'F', 'B', 'A', 'D', 'E'}

