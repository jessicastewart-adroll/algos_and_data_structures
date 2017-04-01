graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
def bfs_all_paths(graph, start, end):
  queue = [(start, [start])]
  paths = []
  
  while queue:
    node, path = queue.pop(0)
    for adj in graph[node]:
      if adj not in path:
        if adj == end:
          paths.append(path+[end])
        else:
          queue.append((adj, path+[adj]))
  
        
  return paths      
  
print(bfs_all_paths(graph, 'A', 'F'))
# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
