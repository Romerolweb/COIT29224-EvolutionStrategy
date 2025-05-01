from es_optimiser.objective_functions import sphere_function
from es_optimiser.evolution_strategy import evolution_strategy

def main():
    # Define problem parameters
    dim = 10  # Dimensionality of the problem
    population_size = 50
    generations = 100
    sigma = 0.1

    # Run Evolution Strategy
    best_solution, best_fitness = evolution_strategy(
        objective_function=sphere_function,
        dim=dim,
        population_size=population_size,
        generations=generations,
        sigma=sigma
    )

    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness: {best_fitness}")

if __name__ == "__main__":
    main()