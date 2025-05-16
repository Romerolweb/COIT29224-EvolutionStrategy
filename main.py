import logging
from datetime import datetime
import time
import os
import es_optimiser
import numpy as np
from es_optimiser.evolution_strategy import EvolutionStrategy
from es_optimiser.objective_functions import rastrigin
from es_optimiser.plot import plot_convergence, plot_rastrigin_2d_landscape

def run_es_optimization(selection_strategy, random_seed, run_label=None):
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

    start_time = time.time()

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

    best_found = es_optimizer.get_best_solution()
    convergence_history = es_optimizer.get_history()

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

    # --- Save plots ---
    if run_label is None:
        run_label = f"{selection_strategy.replace(' ', '').replace(',', '').replace('+', 'plus')}_seed{random_seed}"
    # Save convergence plot
    if convergence_history:
        plot_convergence(
            convergence_history,
            title=f"Convergence ({selection_strategy}, seed={random_seed})",
            filename=f"convergence_{run_label}.png"
        )
    # Save 2D landscape plot if 2D
    if best_found is not None and PROBLEM_DIMENSIONS == 2:
        plot_rastrigin_2d_landscape(
            bounds=SEARCH_BOUNDS,
            best_solution=best_found.genotype,
            filename=f"landscape_{run_label}.png"
        )

    return elapsed_time, best_found, convergence_history

if __name__ == "__main__":
    selection_strategies = ['(mu, lambda)', '(mu + lambda)']
    random_seeds = [123, 332, 456, 789, 101, 202, 303, 404]  # 8 seeds for 16 runs

    results = []
    for i, selection_strategy in enumerate(selection_strategies):
        for j, random_seed in enumerate(random_seeds):
            run_label = f"{'A' if i == 0 else 'B'}{j+1}"
            print(f"Running ES with {selection_strategy} and seed {random_seed} (Run {run_label})...")
            elapsed_time, best_found, _ = run_es_optimization(selection_strategy, random_seed, run_label=run_label)
            results.append({
                "Run Label": run_label,
                "Selection Strategy": selection_strategy,
                "Random Seed": random_seed,
                "Elapsed Time (s)": elapsed_time,
                "Best Solution": best_found.genotype if best_found else None,
                "Distance to Origin": np.linalg.norm(best_found.genotype) if best_found else None
            })

    print("\n--- Grid Search Results ---")
    for result in results:
        print(result)