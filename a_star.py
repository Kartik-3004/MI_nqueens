import numpy as np
from queue import PriorityQueue

def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_8_queens_a_star():
    initial_board = np.zeros((8, 8), dtype=int)
    open_set = PriorityQueue()
    # Change: Store board information as a string initially to avoid direct comparison
    open_set.put((8, 0, initial_board.tobytes(), []))

    while not open_set.empty():
        _, cost, board_bytes, path = open_set.get()
        board = np.frombuffer(board_bytes, dtype=int).reshape(8, 8) # Change: Convert back to numpy array

        if cost == 8:
            return board, path

        for i in range(8):
            if is_valid(board, i, cost):
                new_board = np.copy(board)
                new_board[i][cost] = 1
                new_path = path + [(i, cost)]
                heuristic = 8 - (cost + 1)
                # Change: Store the board as bytes again
                open_set.put((cost + 1 + heuristic, cost + 1, new_board.tobytes(), new_path))

    return None, None

board, path = solve_8_queens_a_star()
if board is not None:
    print("Solution found:")
    print(board)
else:
    print("No solution found.")
