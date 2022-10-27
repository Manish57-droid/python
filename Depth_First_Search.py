graph={
'A': ['B','C'],
'B': ['D','E'],
'C': ['F','G'],
'D': ['B'],
'E': ['B'],
'F': ['C'],
'G': ['C']
}

visited = set() 

def dfs(visited, graph, node):
    
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
