import logging
from datetime import datetime
import time
import os
import es_optimiser
import numpy as np
from es_optimiser.evolution_strategy import EvolutionStrategy
from es_optimiser.objective_functions import rastrigin
from es_optimiser.plot import plot_convergence

# Configure logging
log_filename = "es_optimization.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'  # Append to the log file
)

def run_es_optimization(selection_strategy, random_seed):
    """Run a single ES optimization with the given selection strategy and random seed."""
    # --- Configuration ---
    PROBLEM_DIMENSIONS = 2
    SEARCH_BOUNDS = (-5.12, 5.12)
    POPULATION_MU = 30
    OFFSPRING_LAMBDA = 200
    GENERATIONS = 250
    MUTATION_SIGMA = 0.2

    logging.info("========================================")
    logging.info(f"Run started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Starting ES Optimization with the following configuration:")
    logging.info(f"SELECTION_STRATEGY: {selection_strategy}")
    logging.info(f"RANDOM_SEED: {random_seed}")

    # --- Timing the Optimization ---
    start_time = time.time()

    # --- Instantiate and Run ES ---
    es_optimizer = EvolutionStrategy(
        objective_function=rastrigin,
        dimensions=PROBLEM_DIMENSIONS,
        bounds=SEARCH_BOUNDS,
        mu=POPULATION_MU,
        lambda_=OFFSPRING_LAMBDA,
        max_generations=GENERATIONS,
        sigma=MUTATION_SIGMA,
        selection_type=selection_strategy,
        seed=random_seed
    )

    es_optimizer.run()

    end_time = time.time()
    elapsed_time = end_time - start_time

    # --- Retrieve Results ---
    best_found = es_optimizer.get_best_solution()
    convergence_history = es_optimizer.get_history()

    # --- Log Results ---
    if best_found:
        distance_to_origin = np.linalg.norm(best_found.genotype)
        logging.info("Optimization completed successfully.")
        logging.info(f"Best Individual Found: {best_found}")
        logging.info(f"Distance from Origin (Global Optimum): {distance_to_origin:.4e}")
        logging.info(f"Elapsed Time: {elapsed_time:.2f} seconds")
    else:
        logging.warning("Optimization did not complete successfully or find a best individual.")

    logging.info(f"Run ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Total Elapsed Time: {elapsed_time:.2f} seconds")
    logging.info("========================================")

    return elapsed_time, best_found, convergence_history

if __name__ == "__main__":
    # Define grid search parameters
    selection_strategies = ['(mu, lambda)', '(mu + lambda)']
    random_seeds = [123, 332, 456, 789]  # Add more seeds for diversity

    # Perform grid search
    results = []
    for selection_strategy in selection_strategies:
        for random_seed in random_seeds:
            print(f"Running ES with {selection_strategy} and seed {random_seed}...")
            elapsed_time, best_found, _ = run_es_optimization(selection_strategy, random_seed)
            results.append({
                "Selection Strategy": selection_strategy,
                "Random Seed": random_seed,
                "Elapsed Time (s)": elapsed_time,
                "Best Solution": best_found.genotype if best_found else None,
                "Distance to Origin": np.linalg.norm(best_found.genotype) if best_found else None
            })

    # Print summary of results
    print("\n--- Grid Search Results ---")
    for result in results:
        print(result)