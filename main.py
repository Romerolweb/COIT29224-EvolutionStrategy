
# es_optimiser/main.py

from es_optimiser.evolution_strategy import EvolutionStrategy, Individual # Import Individual if needed
from es_optimiser.objective_functions import rastrigin
from es_optimiser.utils import plot_convergence, plot_rastrigin_2d_landscape
import numpy as np

if __name__ == "__main__":
    # --- Configuration ---
    PROBLEM_DIMENSIONS = 2    # Use 2 for easy visualization, or higher (e.g., 10, 20)
    SEARCH_BOUNDS = (-5.12, 5.12)
    POPULATION_MU = 30      # Number of parents
    OFFSPRING_LAMBDA = 200  # Number of offspring
    GENERATIONS = 250       # Max iterations
    MUTATION_SIGMA = 0.2    # Initial mutation strength (requires tuning!)
    # Choose selection: '(mu, lambda)' or '(mu + lambda)'
    SELECTION_STRATEGY = '(mu, lambda)'
    RANDOM_SEED = 123       # For reproducibility

    print(f"--- Running ES for {PROBLEM_DIMENSIONS}-D Rastrigin Function ---")

    # --- Instantiate and Run ES ---
    es_optimizer = EvolutionStrategy(
        objective_function=rastrigin,
        dimensions=PROBLEM_DIMENSIONS,
        bounds=SEARCH_BOUNDS,
        mu=POPULATION_MU,
        lambda_=OFFSPRING_LAMBDA,
        max_generations=GENERATIONS,
        sigma=MUTATION_SIGMA,
        selection_type=SELECTION_STRATEGY,
        seed=RANDOM_SEED
    )

    es_optimizer.run() # Execute the optimization

    # --- Retrieve Results ---
    best_found: Individual = es_optimizer.get_best_solution()
    convergence_history = es_optimizer.get_history()

    # --- Display Results ---
    if best_found:
        print("\n--- Optimization Results ---")
        # Use the __repr__ of the Individual class
        print(f"Best Individual Found: {best_found}")
        # Check proximity to known optimum (0,0,...,0)
        distance_to_origin = np.linalg.norm(best_found.genotype)
        print(f"Distance from Origin (Global Optimum): {distance_to_origin:.4e}")
    else:
        print("\nOptimization did not complete successfully or find a best individual.")

    # --- Plotting ---
    if convergence_history:
        plot_convergence(convergence_history, title=f"Rastrigin {PROBLEM_DIMENSIONS}D ES Convergence ({SELECTION_STRATEGY})")

    # Plot 2D landscape only if dimensions=2
    if PROBLEM_DIMENSIONS == 2 and best_found:
        plot_rastrigin_2d_landscape(bounds=SEARCH_BOUNDS, best_solution=best_found.genotype)

