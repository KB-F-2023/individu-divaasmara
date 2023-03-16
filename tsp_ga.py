# Case : Networking routing optimization
# A telecommunications company wants to optimize the routing of signals through a network of nodes.
# The network consists of some nodes, and the company wants to find the optimal routing path that minimizes the signal delay.

# Solution :
# 1. Encoding the candidate solution
# 2. Generating the initial population
# 3. Fitness function
# 4. Selection the best candidate solution

# input :
# distances: a 2D matrix of distances between nodes in the network
# population_size: the size of the population
# num_generations: the number of generations to evolve the population
# mutation_rate: the probability of mutation for each candidate solution
# elitism_rate: the percentage of the population that is carried over to the next generation unchanged

# output :
# best_sequence: the sequence of nodes that represents the best routing path found by the algorithm
# best_fitness: the fitness score of the best routing path found by the algorithm

import random

# to generates such a population by randomly shuffling the indices of the cities,
# creating a list of shuffled sequences of length equal to the population size.


def create_population(distances, size):
    cities = len(distances)  # get number from length of the distances matrix
    population = []  # initialize an empty list population.
    for _ in range(size):  # loop size number of times
        # create a list sequence and shuffle using random.sample function
        sequence = random.sample(range(cities), cities)
        # append the shuffled sequence to the population list
        population.append(sequence)
    return population

# to calculates the fitness of a given sequence of cities or
# to evaluate how good a particular sequence is in terms of minimizing the total distance traveled.
# the fitness of a solution is the inverse of the total distance traveled, so the smaller the total distance, the higher the fitness value.


def fitness(sequence, distances):
    total_distance = 0  # initialize a variable total_distance to 0.
    # loop over the indices of the cities in the given sequence.
    for i in range(len(sequence)):
        j = (i + 1) % len(sequence)  # get the index of the next city
        # get the indices of the two cities and save into matrix.
        city_i, city_j = sequence[i], sequence[j]
        # add the distance between the two cities
        total_distance += distances[city_i][city_j]
    return 1 / total_distance

# takes in the current population, distance matrix, elitism rate, and mutation rate as input parameters.
# it is responsible for creating a new population of solutions for the next generation using genetic operations like crossover and mutation.


def evolve_population(population, distances, elitism_rate, mutation_rate):
    # to calculates the fitness score of each solution in the current population
    fitness_scores = [(fitness(seq, distances), seq) for seq in population]
    # sorted in descending order based on the fitness score
    fitness_scores.sort(reverse=True)
    elitism = int(elitism_rate * len(population))
    # top elitism individuals is added to the new_population list
    new_population = [fitness_scores[i][1] for i in range(elitism)]
    # to create new individuals until the new population has the same size as the old population
    while len(new_population) < len(population):
        # to randomly select two individuals from the population without replacement
        parent_1, parent_2 = random.sample(population, 2)
        # to produce a new child individual, which is added to the new population.
        child = crossover(parent_1, parent_2)
        if random.random() < mutation_rate:  # chance for the child will undergo a mutation
            # if the random number generated is less than the mutation rate, then the child is mutated
            child = mutate(child)
        # new child individual is appended to the new population
        new_population.append(child)
    return new_population

# to takes in two parent sequences and performs a crossover operation to produce a child sequence


def crossover(parent_1, parent_2):
    # Randomly choose start and end indices for the crossover segment
    start = random.randint(0, len(parent_1) - 1)
    end = random.randint(start, len(parent_1) - 1)
    # Create a new list to represent the child sequence, initially filled with None values
    child = [None] * len(parent_1)
    for i in range(start, end):  # Copy the crossover segment from parent 1 into the child
        child[i] = parent_1[i]
    # Create a list of remaining values from parent 2 that are not already in the child
    remaining = [x for x in parent_2 if x not in child]
    # Fill in the remaining values in the child with values from parent 2
    j = 0
    for i in range(len(parent_1)):  # to iterate over the indices of the crossover segment
        if child[i] is None:  # to iterates over the values in parent_2 that are not already in child
            # the values that fill in the remaining indices in child that were not part of the crossover segment.
            child[i] = remaining[j]
            j += 1
    return child

# to takes a sequence as input and returns a mutated version of that sequence.


def mutate(sequence):
    # to swap two cities in the sequence.
    start = random.randint(0, len(sequence) - 1)
    # to swap two cities in the sequence
    end = random.randint(0, len(sequence) - 1)
    # the cities at the start and end indices are swapped
    sequence[start], sequence[end] = sequence[end], sequence[start]
    return sequence

# to takes several parameters and returns a list of the best sequences found during the optimization process


def find_best_sequences(distances, population_size, num_generations, elitism_rate, mutation_rate, num_best_sequences):
    # initialize a population of sequences using the create_population function
    population = create_population(distances, population_size)
    best_sequences = []
    for i in range(num_generations):
        population = evolve_population(
            population, distances, elitism_rate, mutation_rate)  # evolve the population using the evolve_population function
        # calculate the fitness score for each sequence in the population
        fitness_scores = [(fitness(seq, distances), seq) for seq in population]
        # sort the sequences by fitness score in descending order
        fitness_scores.sort(reverse=True)
        # append the best sequence and its fitness score to the best_sequences list
        best_sequences.append((fitness_scores[0][1], fitness_scores[0][0]))
    # sort the best_sequences list by fitness score in descending order
    best_sequences.sort(key=lambda pair: pair[1], reverse=True)
    return [(seq, fit) for (seq, fit) in best_sequences[:num_best_sequences]]


# Example usage
distances = [
    [0, 2, 5, 7],
    [2, 0, 4, 8],
    [5, 4, 0, 3],
    [7, 8, 3, 0]
]
population_size = 100
num_generations = 500
mutation_rate = 0.02
elitism_rate = 0.1
num_best_sequences = 3

best_sequences = find_best_sequences(
    distances, population_size, num_generations, elitism_rate, mutation_rate, num_best_sequences)

for i, (sequence, fitness) in enumerate(best_sequences):
    print(f"Sequence {i+1}: {sequence}")
    print(f"Fitness: {fitness}")

# Reference :
# https://github.com/ritu-thombre99/Travelling-Salesman-Problem-using-Genetic-Algorithm
# https://github.com/avitomar12/TSP-using-Genetic-Algorithm
# https://www.geeksforgeeks.org/traveling-salesman-problem-using-genetic-algorithm/
