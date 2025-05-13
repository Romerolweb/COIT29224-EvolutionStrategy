import logging
from datetime import datetime
import time  # Import the time module
import os
import es_optimiser
import numpy as np
from es_optimiser.evolution_strategy import EvolutionStrategy
from es_optimiser.objective_functions import rastrigin
from es_optimiser.plot import plot_convergence, plot_rastrigin_2d_landscape

# Configure logging
log_filename = "es_optimization.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'  # Append to the log file
)

if __name__ == "__main__":
    # --- Configuration ---
    PROBLEM_DIMENSIONS = 2    # Use 2 for easy visualization, or higher (e.g., 10, 20)
    SEARCH_BOUNDS = (-5.12, 5.12)
    POPULATION_MU = 30      # Number of parents
    OFFSPRING_LAMBDA = 200  # Number of offspring
    GENERATIONS = 250       # Max iterations
    MUTATION_SIGMA = 0.2    # Initial mutation strength (requires tuning!)
    SELECTION_STRATEGY = '(mu + lambda)'
    RANDOM_SEED = 123       # For reproducibility

    # Log hyperparameter configuration
    logging.info("========================================")
    logging.info(f"Run started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info("Starting ES Optimization with the following configuration:")
    logging.info(f"PROBLEM_DIMENSIONS: {PROBLEM_DIMENSIONS}")
    logging.info(f"SEARCH_BOUNDS: {SEARCH_BOUNDS}")
    logging.info(f"POPULATION_MU: {POPULATION_MU}")
    logging.info(f"OFFSPRING_LAMBDA: {OFFSPRING_LAMBDA}")
    logging.info(f"GENERATIONS: {GENERATIONS}")
    logging.info(f"MUTATION_SIGMA: {MUTATION_SIGMA}")
    logging.info(f"SELECTION_STRATEGY: {SELECTION_STRATEGY}")
    logging.info(f"RANDOM_SEED: {RANDOM_SEED}")

    print(f"--- Running ES for {PROBLEM_DIMENSIONS}-D Rastrigin Function ---")

    # --- Timing the Optimization ---
    start_time = time.time()  # Record the start time

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

    es_optimizer.run()  # Execute the optimization

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time in seconds

    # --- Retrieve Results ---
    best_found = es_optimizer.get_best_solution()
    convergence_history = es_optimizer.get_history()

    # --- Display and Log Results ---
    if best_found:
        print("\n--- Optimization Results ---")
        print(f"Best Individual Found: {best_found}")
        distance_to_origin = np.linalg.norm(best_found.genotype)
        print(f"Distance from Origin (Global Optimum): {distance_to_origin:.4e}")
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")

        # Log results
        logging.info("Optimization completed successfully.")
        logging.info(f"Best Individual Found: {best_found}")
        logging.info(f"Distance from Origin (Global Optimum): {distance_to_origin:.4e}")
        logging.info(f"Elapsed Time: {elapsed_time:.2f} seconds")
    else:
        print("\nOptimization did not complete successfully or find a best individual.")
        logging.warning("Optimization did not complete successfully or find a best individual.")

    # --- Plotting ---
    if convergence_history:
        print("\n--- Plotting Convergence History ---")
        plot_convergence(convergence_history, title=f"Rastrigin {PROBLEM_DIMENSIONS}D ES Convergence ({SELECTION_STRATEGY})")
        logging.info("Convergence history plotted.")

    if PROBLEM_DIMENSIONS == 2 and best_found:
        print("\n--- Plotting Rastrigin 2D Landscape ---")
        plot_rastrigin_2d_landscape(bounds=SEARCH_BOUNDS, best_solution=best_found.genotype)
        logging.info("2D landscape plotted.")

    logging.info(f"Run ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Total Elapsed Time: {elapsed_time:.2f} seconds")
    logging.info("========================================")