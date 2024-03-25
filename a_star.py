import numpy as np
import time
import tracemalloc
from queue import PriorityQueue

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def non_attacking_pairs(board):
    non_attacking = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] != -1 and board[j] != -1:
                if board[i] != board[j] and abs(board[i] - board[j]) != j - i:
                    non_attacking += 1
    return non_attacking

def solve_8_queens_a_star():
    tracemalloc.start()
    start_time = time.time()
    memory_snapshots = []

    initial_board = np.zeros(8, dtype=int) - 1
    open_set = PriorityQueue()
    open_set.put((0, 0, initial_board.tobytes(), []))

    while not open_set.empty():
        _, cost, board_bytes, path = open_set.get()
        board = np.frombuffer(board_bytes, dtype=int)
        col = len(path)

        snapshot = tracemalloc.take_snapshot()
        memory_snapshots.append(snapshot)

        if col == 8:
            end_time = time.time()
            peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
            tracemalloc.stop()
            
            average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
            time_taken_ms = (end_time - start_time) * 1000

            final_board = np.zeros((8, 8), dtype=int)
            for i, row in enumerate(path):
                final_board[row][i] = 1
            
            return final_board, path, time_taken_ms, peak_memory_kb, average_memory_kb

        for row in range(8):
            if is_safe(board, row, col):
                new_board = np.copy(board)
                new_board[col] = row
                new_path = path + [row]
                new_heuristic = -non_attacking_pairs(new_board)
                open_set.put((new_heuristic, col + 1, new_board.tobytes(), new_path))

    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    tracemalloc.stop()

    average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
    time_taken_ms = (end_time - start_time) * 1000

    return None, None, time_taken_ms, peak_memory_kb, average_memory_kb

def print_board(board):
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))

board, path, time_taken_ms, peak_memory_kb, average_memory_kb = solve_8_queens_a_star()

if board is not None:
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")

print(f"Time taken: {time_taken_ms:.2f} ms")
print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
print(f"Average memory used (approx.): {average_memory_kb / 1024:.2f} MB")
