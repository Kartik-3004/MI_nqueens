import numpy as np
import random
import time
import tracemalloc

def calculate_attacks(board):
    attacking_pairs = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacking_pairs += 1
    return attacking_pairs

def get_neighbors(board):
    neighbors = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] != j:
                neighbor = list(board)
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(board):
    tracemalloc.start()
    start_time = time.time()
    memory_snapshots = []

    current_board = board
    current_attacks = calculate_attacks(current_board)
    while True:
        snapshot = tracemalloc.take_snapshot()
        memory_snapshots.append(snapshot)

        neighbors = get_neighbors(current_board)
        next_board = None
        next_attacks = current_attacks
        for neighbor in neighbors:
            attacks = calculate_attacks(neighbor)
            if attacks < next_attacks:
                next_board = neighbor
                next_attacks = attacks
        if next_attacks == current_attacks:
            break
        current_board = next_board
        current_attacks = next_attacks

    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    
    total_memory_size = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots if snapshot.statistics('filename')) / 1024
    average_memory_kb = total_memory_size / len(memory_snapshots) if memory_snapshots else 0
    
    time_taken_ms = (end_time - start_time) * 1000
    tracemalloc.stop()

    return current_board, time_taken_ms, peak_memory_kb, average_memory_kb

def print_board(board):
    for row in range(8):
        print(' '.join('Q' if col == board[row] else '.' for col in range(8)))

def solve_8_queens_hill_climbing():
    initial_board = [random.randint(0, 7) for _ in range(8)]
    solution_board, time_taken_ms, peak_memory_kb, average_memory_kb = hill_climbing(initial_board)
    print_board(solution_board) 
    print(f"Time taken: {time_taken_ms:.2f} ms")
    print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
    print(f"Average memory used (approx.): {average_memory_kb / 1024:.3f} MB")

solve_8_queens_hill_climbing()
