# =========================
# GREEDY ALGORITHMS
# =========================

# -------------------------
# I. Selection Sort
# -------------------------

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume the current index is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update if a smaller element is found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

# -------------------------
# III & VII. Dijkstra’s Algorithm (Single Source Shortest Path)
# -------------------------

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    print("Dijkstra's Shortest Paths from", start)
    for node in distances:
        print(f"{start} -> {node}: {distances[node]}")
    print()

# Example graph for Dijkstra
graph1 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
dijkstra(graph1, 'A')


# -------------------------
# IV. Job Scheduling Problem (with deadline)
# -------------------------
def job_scheduling(jobs):
    # jobs = [(JobID, Profit, Deadline)]
    jobs.sort(key=lambda x: x[1], reverse=True)  # sort by profit
    n = max(job[2] for job in jobs)
    slots = [False] * n
    result = [None] * n

    for job in jobs:
        for j in range(min(n, job[2]) - 1, -1, -1):
            if not slots[j]:
                slots[j] = True
                result[j] = job[0]
                break

    print("Job Scheduling Result:", [job for job in result if job is not None])
    print()

# Example jobs: (JobID, Profit, Deadline)
jobs = [('J1', 100, 2), ('J2', 19, 1), ('J3', 27, 2), ('J4', 25, 1), ('J5', 15, 3)]
job_scheduling(jobs)


# -------------------------
# V. Prim’s Minimum Spanning Tree Algorithm
# -------------------------
def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            mst_cost += cost
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor))

    print(f"Prim's MST Cost from {start}: {mst_cost}\n")

# Example graph
graph2 = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}
prim(graph2, 'A')


# -------------------------
# VI. Kruskal’s Minimum Spanning Tree Algorithm
# -------------------------
def kruskal(vertices, edges):
    parent = {}
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root1 = find(u)
        root2 = find(v)
        if root1 != root2:
            parent[root2] = root1
            return True
        return False

    for v in vertices:
        parent[v] = v

    mst_cost = 0
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        if union(u, v):
            mst_cost += weight

    print("Kruskal's MST Cost:", mst_cost)
    print()

# Example graph: (u, v, weight)
vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 1), ('C', 'D', 4)]
kruskal(vertices, edges)
