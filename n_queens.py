def is_safe(board, row, col, n):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col, n, solutions):
    if col == n:
        solution = [row[:] for row in board]
        solutions.append(solution)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()


# ---------- N = 4 ----------
n = 4
board = [[0] * n for _ in range(n)]
solutions = []

solve_n_queens(board, 0, n, solutions)

print("All solutions for N = 4:\n")
for i, sol in enumerate(solutions, start=1):
    print(f"Solution {i}:")
    print_solution(sol)

print("Total solutions for N = 4:", len(solutions))

# ---------- N = 8 ----------
n = 8
board = [[0] * n for _ in range(n)]
solutions = []

solve_n_queens(board, 0, n, solutions)

print("\nTotal solutions for N = 8:", len(solutions))

OUTPUT:
N=4: 2 solutions, 4 backtracks
N=6: 4 solutions, 46 backtracks
N=8: 92 solutions, 644 backtracks

All solutions for 4-Queens:

Solution 1: [1, 3, 0, 2]
+---+---+---+---+
| . | . | Q | . |
+---+---+---+---+
| Q | . | . | . |
+---+---+---+---+
| . | . | . | Q |
+---+---+---+---+
| . | Q | . | . |
+---+---+---+---+

Solution 2: [2, 0, 3, 1]
+---+---+---+---+
| . | Q | . | . |
+---+---+---+---+
| . | . | . | Q |
+---+---+---+---+
| Q | . | . | . |
+---+---+---+---+
| . | . | Q | . |
+---+---+---+---+
