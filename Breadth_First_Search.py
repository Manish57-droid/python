graph={
'A': ['B','C'],
'B': ['D','E'],
'C': ['F','G'],
'D': ['B'],
'E': ['B'],
'F': ['C'],
'G': [ 'C']
}

visited=[]

def BFS (visited,graph, node, target):
    queue=[]
    queue.append(node)
    visited.append(node)
    
    while queue:
        m=queue.pop(0)
        if(m==target):
            print("\nfound",m)
            break
        
        print(m, end="")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
BFS(visited,graph,'A','G')
