import numpy as np
import random
import time
import tracemalloc

def generate_individual():
    return np.random.permutation(8)

def compute_fitness(individual):
    collisions = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if abs(i - j) == abs(individual[i] - individual[j]):
                collisions += 1
    return 28 - collisions  

def selection(population, fitnesses):
    idx = np.random.choice(np.arange(len(population)), size=2, replace=False, p=fitnesses/fitnesses.sum())
    return population[idx[0]], population[idx[1]]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return child1, child2

def mutate(individual):
    idx = range(len(individual))
    i1, i2 = random.sample(idx, 2)
    individual[i1], individual[i2] = individual[i2], individual[i1]

def solve_8_queens_genetic(population_size=100, generations=1000):
    tracemalloc.start()
    start_time = time.time()
    memory_snapshots = []

    population = [generate_individual() for _ in range(population_size)]
    total_generations = 0
    
    for generation in range(generations):
        total_generations += 1
        fitnesses = np.array([compute_fitness(ind) for ind in population])
        
        snapshot = tracemalloc.take_snapshot()
        memory_snapshots.append(snapshot)
        
        if np.max(fitnesses) == 28:
            solution = population[np.argmax(fitnesses)]
            break 
        
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < 0.1:
                mutate(child1)
                mutate(child2)
            new_population.extend([child1, child2])
        
        population = new_population
    
    end_time = time.time()
    peak_memory_kb = tracemalloc.get_traced_memory()[1] / 1024
    average_memory_kb = sum(snapshot.statistics('filename')[0].size for snapshot in memory_snapshots) / len(memory_snapshots) / 1024
    time_taken_ms = (end_time - start_time) * 1000
    tracemalloc.stop()
    
    if 'solution' not in locals(): 
        print("No solution found after the maximum allowed generations.")
        solution = None

    return solution, total_generations, time_taken_ms, peak_memory_kb, average_memory_kb

def print_board(solution):
    board = np.zeros((8, 8), dtype=str)
    board[:, :] = '.'
    for col, row in enumerate(solution):
        board[row, col] = 'Q'
    for row in board:
        print(' '.join(row))

solution, total_generations, time_taken_ms, peak_memory_kb, average_memory_kb = solve_8_queens_genetic()

if solution is not None:
    print(f"Solution found:")
    print_board(solution)
    print(f"Number of generations until solution: {total_generations}")
else:
    print(f"No solution found within {total_generations} generations.")

print(f"Time taken: {time_taken_ms:.2f} ms")
print(f"Peak memory used: {peak_memory_kb / 1024:.3f} MB")
print(f"Average memory used (approx.): {average_memory_kb / 1024:.2f} MB")
