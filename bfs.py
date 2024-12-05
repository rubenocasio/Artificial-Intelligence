from collections import deque

graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def bfs(graph, start):
    visited = set()      # Set to track visited nodes
    queue = deque([start])  # Queue for BFS
    visited.add(start)   # Mark the start node as visited
    
    while queue:
        node = queue.popleft()  # Dequeue the first element
        print(node, end=" ")    # Process the current node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # Add unvisited neighbors to the queue
                visited.add(neighbor)   # Mark them as visited

bfs(graph, 'A')
