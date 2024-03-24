import numpy as np
import time
import tracemalloc

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_dfs(board, path, col, memory_snapshots):
    if col == len(board):
        return True, board, path
    
    for row in range(len(board)):
        if is_safe(path, row, col):
            board[row][col] = 1
            path.append(row)
            
            snapshot = tracemalloc.take_snapshot()
            memory_snapshots.append(snapshot)
            
            success, solved_board, solved_path = solve_dfs(board, path, col + 1, memory_snapshots)
            if success:
                return True, solved_board, solved_path

            # Backtrack
            board[row][col] = 0
            path.pop()

    return False, None, None

def solve_8_queens_dfs():
    tracemalloc.start()
    start_time = time.time()
    memory_snapshots = []

    board = np.zeros((8, 8), dtype=int)
    solved, solved_board, path = solve_dfs(board, [], 0, memory_snapshots)

    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
    time_taken_ms = (end_time - start_time) * 1000
    
    tracemalloc.stop()

    return solved_board, path, time_taken_ms, peak_memory_kb, average_memory_kb

def print_board(board):
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))

board, path, time_taken_ms, peak_memory_kb, average_memory_kb = solve_8_queens_dfs()

if board is not None:
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")

print(f"Time taken: {time_taken_ms:.2f} ms")
print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
print(f"Average memory used (approx.): {average_memory_kb / 1024:.2f} MB")
