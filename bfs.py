import numpy as np
import time
import tracemalloc
from collections import deque

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_8_queens_bfs():
    tracemalloc.start()
    start_time = time.time()
    memory_snapshots = []

    queue = deque()
    queue.append((np.zeros((8, 8), dtype=int), []))
    while queue:
        board, path = queue.popleft()
        col = len(path)

        snapshot = tracemalloc.take_snapshot()
        memory_snapshots.append(snapshot)

        if col == 8:
            end_time = time.time()
            peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
            tracemalloc.stop()
            
            average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
            time_taken_ms = (end_time - start_time) * 1000
            
            return board, path, time_taken_ms, peak_memory_kb, average_memory_kb

        for row in range(8):
            if is_safe(path, row, col):
                new_board = np.copy(board)
                new_board[row][col] = 1
                new_path = path + [row] 
                queue.append((new_board, new_path))

    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()

    average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
    time_taken_ms = (end_time - start_time) * 1000

    return None, None, time_taken_ms, peak_memory_kb, average_memory_kb

def print_board(board):
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))

board, path, time_taken_ms, peak_memory_kb, average_memory_kb = solve_8_queens_bfs()

if board is not None:
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")

print(f"Time taken: {time_taken_ms:.2f} ms")
print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
print(f"Average memory used (approx.): {average_memory_kb / 1024:.2f} MB")
