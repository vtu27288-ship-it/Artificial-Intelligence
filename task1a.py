def dfs(graph, start):
    stack, visited = [start], set()
    print("DFS:", end=" ")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Add neighbors in reversed order to visit in correct order
            stack.extend(reversed([neighbor for neighbor in graph[node] if neighbor not in visited]))
    print()

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')
