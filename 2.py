import heapq

# Directions: up, down, left, right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # reverse path

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

# Example grid: 0 = free, 1 = obstacle
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid, start, goal)
print("Path found:", path)


























'''
1. Approach

Language: Python, due to simple syntax and built-in data structures.

Data Structures:

Priority Queue (Min-Heap) using heapq for efficient node selection.

Dictionary to store g (cost), f (total cost), and parent.

Game Problem: We'll implement a simple 2D grid (like pathfinding in a maze or game map) with obstacles.

Heuristic: Use Manhattan distance (|x1 − x2| + |y1 − y2|) — commonly used and simple for grid movement.

2. Theory

A* Algorithm:
Type: Informed search algorithm.

Purpose: Finds shortest path using both actual cost (g) and estimated cost (h).

Formula: f(n) = g(n) + h(n)

g(n): Actual cost from start to node n.

h(n): Heuristic estimate from node n to goal.

Heuristic Used: Manhattan (for grids), Euclidean (for open space).

Data Structure: Priority queue for selecting node with lowest f(n).

Advantages:
More optimal and efficient than Dijkstra if a good heuristic is used.

Guarantees shortest path if h(n) is admissible (never overestimates cost).

Applications:
Pathfinding in games (e.g., Pac-Man, maps), robotics, puzzle solving.
'''