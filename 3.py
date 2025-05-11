def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume the current index is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update if a smaller element is found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)





























'''
1. Approach

Language: Python (simple to write and understand).

Greedy Principle: At each step, select the smallest (or largest) element and place it in the correct sorted position.

Why Greedy? Selection Sort is greedy because it always makes the locally optimal choice (smallest element) hoping it leads to a globally sorted array.

2. Theory

Selection Sort (Greedy Algorithm):
Idea: Repeatedly find the minimum element from the unsorted part and move it to the beginning.

Type: Greedy algorithm.

Time Complexity:

Best / Worst / Average: O(n²)

Space Complexity: O(1) (in-place sorting).

Stability: Not stable by default.

Greedy Justification: At every iteration, it greedily picks the smallest item and places it in the sorted section.

Steps:
Start from index i = 0.

Find the minimum in the remaining array i to n-1.

Swap with element at index i.

Repeat for all i.

Applications:
Simple, intuitive sorting (good for small datasets).

Useful in teaching Greedy concepts.
'''