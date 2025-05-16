# COIT29224 Evolution Strategy Optimizer

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL) 

## Report

For detailed explanations, methodology, and results, see the [project report](./report.md).

## Overview

This repository provides a Python implementation of an **Evolution Strategy (ES)** algorithm tailored for optimizing **multi-modal objective functions**. The core objective is to effectively navigate complex search landscapes with numerous local optima to locate the global optimum.

Developed for **Assignment 2** of the **COIT29224 Evolutionary Computation** course at CQUniversity, this project demonstrates key ES concepts including:
*   Population-based stochastic search.
*   Variation through Gaussian mutation.
*   Configurable survival selection mechanisms: **(μ, λ)** and **(μ + λ)**.

The implementation prioritizes **clarity**, **modularity**, **robust documentation** (docstrings and type hints), and ease of **configuration**.

## Key Features

*   Modular implementation using Python classes (`EvolutionStrategyClarified`, `Individual`).
*   Supports both **(μ, λ)** [comma] and **(μ + λ)** [plus] survival selection strategies.
*   Employs **Gaussian mutation** with configurable strength (`sigma`) for exploration.
*   Includes **boundary handling** via simple clipping to maintain solutions within specified constraints.
*   Features the **Rastrigin function** as a primary multi-modal benchmark example.
*   Easily extensible to include other objective functions.
*   Generates **convergence plots** (Best Fitness vs. Generation) using Matplotlib.
*   Provides optional **2D landscape visualization** for 2-dimensional problems.
*   Adheres to Python best practices for documentation and code organization.

## Project Structure

```
.
├── LICENSE                         # Project license (GPL)
├── README.md                       # This documentation file
├── es_optimiser/                   # Main Python package for ES logic
│   ├── __init__.py                 # Package initializer
│   ├── __pycache__/                # Python bytecode cache
│   ├── evolution_strategy.py       # ES algorithm implementation
│   ├── objective_functions.py      # Fitness/objective functions (e.g., Rastrigin)
│   └── plot.py                     # Plotting utilities
├── es_optimization_A1.log          # Example log file (one for the firs runs after standarising the log format)
├── log_6e93dd33-88cb-4382-a962-b907568a327a.log # Example log file
├── main.py                         # Main script to run the optimizer
├── plan-to-develop.md              # Future deevelopment notes
├── requirements.txt                # Python package dependencies
├── plots/                          # Output plots directory
│   ├── 6e93dd33-88cb-4382-a962-b907568a327a/ # Example run-specific plots
│   └── plots.md                    # Plot documentation/notes
└── report.md                       # Project report
```

## Installation Requirements

*   Python 3.8 or newer
*   NumPy
*   Matplotlib

### Steps:

1.  **Clone the repository:**
    ```bash
    git clone github.com/Romerolweb/COIT29224-EvolutionStrategy
    cd COIT29224-EvolutionStrategy
    ```
2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # Create environment
    python -m venv venv

    # Activate environment
    # Linux/macOS:
    source venv/bin/activate
    # Windows (Command Prompt/PowerShell):
    .\venv\Scripts\activate
    ```

3.  **Install required packages:**
    ```bash
    pip install numpy matplotlib
    ```

## How to Run

Execute the main script from the root directory of the project:

```bash
python main.py
```

**Expected Output:**
1.  The script will print the current ES configuration settings.
2.  It will show progress updates during the optimization process.
3.  Upon completion, it will print the best fitness value found and the corresponding solution vector.
4.  A Matplotlib window will display the convergence plot (best fitness over generations).
5.  If `PROBLEM_DIMENSIONS` in `main.py` is set to `2`, a second plot visualizing the 2D objective function landscape and the best found solution will appear.

## Configuration

Adjust the parameters of the Evolution Strategy directly within the `main.py` script, primarily within the `if __name__ == "__main__":` block:

*   `PROBLEM_DIMENSIONS`: Integer, sets the dimensionality of the search space.
*   `SEARCH_BOUNDS`: Tuple `(min_bound, max_bound)` defining the limits for each variable.
*   `POPULATION_MU`: Integer (`μ`), the number of parents selected each generation.
*   `OFFSPRING_LAMBDA`: Integer (`λ`), the number of offspring generated each generation.
*   `GENERATIONS`: Integer, the maximum number of generations the algorithm will run.
*   `MUTATION_SIGMA`: Float, the standard deviation (`σ`) for Gaussian mutation, controlling step size.
*   `SELECTION_STRATEGY`: String, either `'(mu, lambda)'` or `'(mu + lambda)'`.
*   `RANDOM_SEED`: Integer or `None`, for reproducible results.
*   `objective_function`: The function handle to optimize (e.g., `rastrigin`). Change this to use a different function.

## Adding Objective Functions

To add a new function to optimize:
1.  Define the function in `es_optimiser/objective_functions.py`.
2.  Ensure the function accepts a single argument: a **NumPy array** representing the candidate solution (`x`).
3.  Ensure the function returns a single **float** value representing the fitness (lower is better for minimization).
4.  Update the `objective_function` variable in `main.py` to point to your new function (e.g., `objective_function=my_new_function`).

---

## License

This project is an academic project. See license in ./LICENSE

---

## Author Information

*   **Author:** `Sebastian Romero Laguna`
*   **Course:** COIT29224 Evolutionary Computation
*   **Institution:** CQUniversity
*   **Assignment:** Assignment 2, Term 1, 2025

---
