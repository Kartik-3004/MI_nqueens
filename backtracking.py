import time
import tracemalloc
import numpy as np

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_queens_backtracking(board, col, memory_snapshots):
    if col >= len(board):
        return True 
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[col] = i 
            snapshot = tracemalloc.take_snapshot()
            memory_snapshots.append(snapshot)
            solved = solve_queens_backtracking(board, col + 1, memory_snapshots)
            if solved:
                return True
            board[col] = -1 
    
    return False 

def print_board(board):
    for row in board:
        line = ['Q' if col == row else '.' for col in range(len(board))]
        print(' '.join(line))

def solve_8_queens_backtracking():
    n = 8 
    board = [-1] * n
    memory_snapshots = []

    tracemalloc.start()
    start_time = time.time()
    
    solved = solve_queens_backtracking(board, 0, memory_snapshots)
    
    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()

    time_taken_ms = (end_time - start_time) * 1000
    average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
    
    if solved:
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")
    
    print(f"Time taken: {time_taken_ms:.2f} ms")
    print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
    print(f"Average memory used (approx.): {average_memory_kb / 1024:.2f} MB")

solve_8_queens_backtracking()
