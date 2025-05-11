def print_board(board):
    for row in board:
        print(" ".join('Q' if x else '.' for x in row))
    print()

def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]
    cols = [False]*n
    diag1 = [False]*(2*n-1)  # Top-left to bottom-right diagonals
    diag2 = [False]*(2*n-1)  # Top-right to bottom-left diagonals

    def backtrack(row):
        if row == n:
            print_board(board)
            return

        for col in range(n):
            if not cols[col] and not diag1[row+col] and not diag2[row-col+n-1]:
                board[row][col] = 1
                cols[col] = diag1[row+col] = diag2[row-col+n-1] = True

                backtrack(row + 1)  # Recurse for next row

                # Backtrack
                board[row][col] = 0
                cols[col] = diag1[row+col] = diag2[row-col+n-1] = False

    backtrack(0)

solve_n_queens(4)


























'''
1. Approach

Language: Python – clean recursion, easy state tracking.

Problem: Place n queens on an n x n chessboard such that no two queens attack each other.

Techniques:

Backtracking: Explore possibilities row-by-row, backtrack on conflicts.

Branch and Bound: Improve efficiency by pruning branches using bounding conditions (e.g., tracking columns and diagonals).

2. Theory

N-Queens Problem:
Goal: Place n queens on an n x n board so that no two queens threaten each other (same row, column, or diagonal).

Type: Constraint Satisfaction Problem (CSP).

Constraints:

Only one queen per row.

No two queens on same column or diagonal.

Backtracking:
Idea: Try placing a queen row-by-row.

If a conflict occurs, backtrack and try another column.

Worst Case Time Complexity: O(n!)

Branch and Bound:
Idea: Prune branches early using bounding conditions (e.g., used columns and diagonals).

Improvement over pure backtracking: Avoid exploring obviously invalid states.

Applications:
Chess engines

Scheduling

Puzzle solving

General CSPs
'''