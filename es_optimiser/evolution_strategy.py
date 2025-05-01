import random

def evolution_strategy(objective_function, dim, population_size=50, generations=100, sigma=0.1):
    """Basic Evolution Strategy implementation."""
    # Initialize population
    population = [([random.uniform(-5, 5) for _ in range(dim)], None) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate fitness
        population = [(individual, objective_function(individual)) for individual, _ in population]
        population.sort(key=lambda x: x[1])  # Sort by fitness (minimization)

        # Select top individuals
        top_individuals = population[:population_size // 2]

        # Generate offspring
        offspring = []
        for parent, _ in top_individuals:
            child = [gene + random.gauss(0, sigma) for gene in parent]
            offspring.append((child, None))

        # Replace population with offspring
        population = top_individuals + offspring

    # Return the best solution
    best_individual, best_fitness = min(population, key=lambda x: x[1])
    return best_individual, best_fitness