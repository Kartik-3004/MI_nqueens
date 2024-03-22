from collections import deque

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_8_queens_bfs():
    """Solve the 8 Queens problem using BFS and return one solution and the number of steps."""
    queue = deque()
    queue.append([])  # Start with an empty solution
    steps = 0  # Track the number of steps
    while queue:
        solution = queue.popleft()
        steps += 1  # Increment steps for each solution taken from the queue
        col = len(solution)
        if col == 8:
            return solution, steps  # Return the solution and the number of steps when found
        for row in range(8):
            if is_safe(solution, row, col):
                queue.append(solution + [row])  # Append new row position
    return None, steps  # If no solution is found

def print_solution(solution):
    """Print the chessboard with the queens placed."""
    for row in range(8):
        line = ""
        for col in range(8):
            if col == solution[row]:
                line += "Q "
            else:
                line += ". "
        print(line)

solution, steps = solve_8_queens_bfs()
if solution:
    print(f"A solution to the 8 Queens problem was found in {steps} steps:")
    print_solution(solution)
else:
    print(f"No solution found. Number of steps taken: {steps}.")
