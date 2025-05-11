from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, node, visited = None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end = ' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
            
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end = ' ')
            visited.add(node)
            queue.extend(graph[node])

print('DFS Traversal: ')
dfs(graph, 'A')

print()
print()

print('BFS Traversal: ')
bfs(graph, 'A')





















"""
1. Approach 

Language: Python is best for easy syntax, readability, and handling data structures like graphs using dictionaries/lists.

Graph Representation: Use Adjacency List (dict of lists) — more space-efficient than an adjacency matrix for sparse graphs.

DFS: Naturally recursive — we'll use recursion.

BFS: Uses a queue, so we'll use collections.deque for O(1) pops.


2. Thoery 

Depth First Search (DFS):
Type: Recursive or Stack-based.

Approach: Visit a node → go deep (visit unvisited neighbors recursively).

Time Complexity: O(V + E)

Space Complexity: O(V) due to recursion stack or visited set.

Used in: Topological sort, cycle detection, pathfinding.

Breadth First Search (BFS):
Type: Queue-based (FIFO).

Approach: Visit a node → explore all neighbors before going deeper.

Time Complexity: O(V + E)

Space Complexity: O(V)

Used in: Shortest path in unweighted graphs, level-order traversal.
"""