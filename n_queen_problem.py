def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    # If all queens are placed, add solution to results
    if col >= n:
        solution = ["".join('Q' if cell == 1 else '.' for cell in row) for row in board]
        results.append(solution)
        return

    # Try placing a queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1  # Place queen
            solve_nqueens_util(board, col + 1, n)  # Recur to place the next queen
            board[i][col] = 0  # Backtrack

def solve_nqueens(n, first_row, first_col):
    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # Place the first queen at the specified position
    board[first_row][first_col] = 1

    # Start solving from the next column
    solve_nqueens_util(board, first_col + 1, n)
    return results

# Input
n = 4  # Size of the chessboard
first_row, first_col = 0, 1  # Position of the first queen

# Solve the N-Queens problem
results = []
solutions = solve_nqueens(n, first_row, first_col)

# Output solutions
print(f"Solutions for {n}-Queens with the first queen placed at ({first_row}, {first_col}):")
for solution in solutions:
    for row in solution:
        print(row)
    print()
