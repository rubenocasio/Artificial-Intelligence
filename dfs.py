
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


## Recursive DFS:
def dfs_recursive(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")  # Process the current node
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

dfs_recursive(graph, 'A')

## Iterative DFS:
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the current node
            visited.add(node)
            # Add neighbors to the stack
            stack.extend(graph[node] - visited)

dfs_iterative(graph, 'A')

