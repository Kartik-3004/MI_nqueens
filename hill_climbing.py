import numpy as np
import random

def calculate_attacks(board):
    attacking_pairs = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            # Check if queens are in the same row or on the same diagonal
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacking_pairs += 1
    return attacking_pairs

def get_neighbors(board):
    neighbors = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] != j:
                # Generate a neighbor by moving queen i to a new row j
                neighbor = list(board)
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(board):
    current_board = board
    current_attacks = calculate_attacks(current_board)
    while True:
        neighbors = get_neighbors(current_board)
        next_board = None
        next_attacks = current_attacks
        for neighbor in neighbors:
            attacks = calculate_attacks(neighbor)
            if attacks < next_attacks:
                next_board = neighbor
                next_attacks = attacks
        if next_attacks == current_attacks:
            # No better neighbors found
            break
        current_board = next_board
        current_attacks = next_attacks
    return current_board

# Initialize the board randomly
initial_board = [random.randint(0, 7) for _ in range(8)]
solution_board = hill_climbing(initial_board)

# Print the solution
print("Initial Board (row positions of queens):", initial_board)
print("Attacks:", calculate_attacks(initial_board))
print("Solution Board (row positions of queens):", solution_board)
print("Attacks:", calculate_attacks(solution_board))

# Visualize the solution board
def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

print_board(solution_board)
