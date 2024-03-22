def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        # Check row and diagonal conflicts
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_dfs(board, col, steps):
    """Solve the 8 Queens problem using DFS."""
    if col == len(board):
        return True, steps  # All queens are successfully placed

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[col] = i  # Place queen
            success, steps = solve_dfs(board, col + 1, steps + 1)  # Move to the next column
            if success:
                return True, steps
            # If not successful, backtrack
            board[col] = -1

    return False, steps

def solve_8_queens():
    board = [-1] * 8  # -1 indicates no queen is placed in the column
    solution_found, steps = solve_dfs(board, 0, 0)
    return board, steps if solution_found else 0

solution, steps = solve_8_queens()

if steps > 0:
    print(f"Solution found in {steps} steps:")
    print(solution)
else:
    print("No solution found.")

def print_solution(solution):
    """Print the chessboard with the queens placed."""
    for row in solution:
        line = ""
        for col in range(8):
            if col == row:
                line += "Q "
            else:
                line += ". "
        print(line)

if solution:
    print_solution(solution)
