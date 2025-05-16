"""Main script for running Evolution Strategy optimization on the Rastrigin function."""

import logging
from datetime import datetime
import time
import os
import uuid  # For generating batch UUID
import numpy as np
from es_optimiser.evolution_strategy import EvolutionStrategy
from es_optimiser.objective_functions import rastrigin
from es_optimiser.plot import (
    PLOTS_DIR,
    plot_convergence,
    plot_rastrigin_2d_landscape,
)

# === BATCH SETUP ===
# Generate a unique batch ID for this execution (UUID4)
BATCH_ID = str(uuid.uuid4())
PLOTS_BATCH_DIR = os.path.join(PLOTS_DIR, BATCH_ID)
os.makedirs(PLOTS_BATCH_DIR, exist_ok=True)

# Configure logging: log file is named with the batch ID
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)
# Set up logging configuration
LOG_FILENAME = os.path.join(LOGS_DIR, f"log_{BATCH_ID}.log")
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='w'
)

logging.info("========== BATCH ID: %s ==========", BATCH_ID)
logging.info(
    "Batch started at %s",
    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
)
logging.info("Plots directory: %s", PLOTS_BATCH_DIR)
def run_es_optimization(
    sel_strategy,
    rand_seed,
    run_lbl=None,
):
    """Run Evolution Strategy optimization for a given selection strategy and seed."""
    problem_dimensions = 2
    search_bounds = (-5.12, 5.12)
    population_mu = 30
    offspring_lambda = 200
    generations = 250
    mutation_sigma = 0.2

    if run_lbl is None:
        sel_str = sel_strategy.replace(
            ' ', ''
        ).replace(
            ',', ''
        ).replace(
            '+', 'plus'
        )
        run_lbl = (
            sel_str
            + "_seed"
            + str(rand_seed)
        )

    logging.info("========================================")
    logging.info(
        "Run ID: %s (Batch: %s)",
        run_lbl,
        BATCH_ID,
    )
    logging.info(
        "Run started at %s",
        datetime.now().strftime('%Y-        logging.info(f"2D landscape plot saved: {landscape_plot_path}")

    logging.info(
        f"Run ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Total Elapsed Time: {elapsed_time:.2f} seconds")
    logging.info("========================================")

    return elapsed_time, best_found, convergence_history, convergence_plot_path, landscape_plot_path


if __name__ == "__main__":
    selection_strategies = ['(mu, lambda)', '(mu + lambda)']
    random_seeds = [123, 332, 456, 789, 101,
                    202, 303, 404]  # 8 seeds for 16 runs

    results = []
    for i, selection_strategy in enumerate(selection_strategies):
        for j, random_seed in enumerate(random_seeds):
            run_label = f"{'A' if i == 0 else 'B'}{j+1}"
            print(
                f"Running ES with {selection_strategy} and seed {random_seed} (Run {run_label})...")
            elapsed_time, best_found, _, convergence_plot_path, landscape_plot_path = run_es_optimization(
                selection_strategy, random_seed, run_label=run_label
            )
            results.append({
                "Run Label": run_label,
                "Selection Strategy": selection_strategy,
                "Random Seed": random_seed,
                "Elapsed Time (s)": elapsed_time,
                "Best Solution": best_found.genotype if best_found else None,
                "Distance to Origin": np.linalg.norm(best_found.genotype) if best_found else None,
                "Convergence Plot": convergence_plot_path,
                "Landscape Plot": landscape_plot_path
            })

    print("\n--- Grid Search Results ---")
    for result in results:
        print(result)
