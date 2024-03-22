def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens(board, col, steps):
    """Use backtracking to solve the 8 Queens problem."""
    if col >= len(board):
        return True, steps  # All queens are placed successfully
    
    for i in range(len(board)):
        steps += 1  # Increment steps for each attempt to place a queen
        if is_safe(board, i, col):
            board[col] = i  # Place queen
            solved, steps = solve_queens(board, col + 1, steps)
            if solved:
                return True, steps
            board[col] = -1  # Backtrack
    
    return False, steps  # No position was found

def print_board(board):
    """Print the board."""
    for row in board:
        line = ['Q' if col == row else '.' for col in range(len(board))]
        print(' '.join(line))

n = 8  # Size of the chessboard and number of queens
board = [-1] * n  # Initialize the board with -1, indicating no queen is placed

solved, steps = solve_queens(board, 0, 0)
if solved:
    print("Solution found:")
    print_board(board)
    print(f"Number of steps taken: {steps}")
else:
    print("No solution exists.")
    print(f"Number of steps taken: {steps}")
