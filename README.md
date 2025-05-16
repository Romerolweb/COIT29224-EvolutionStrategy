# COIT29224 Evolution Strategy Optimizer

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL](https://img.shields.io/badge/License-GPL-yellow.svg)](https://opensource.org/licenses/GPL) 

## Overview

This repository provides a modular Python implementation of an **Evolution Strategy (ES)** algorithm for optimizing complex, multi-modal objective functions. The project is designed for **Assignment 2** of the COIT29224 Evolutionary Computation course at CQUniversity, and demonstrates key ES concepts including:
- Population-based stochastic search
- Variation through Gaussian mutation
- Configurable survival selection: **(μ, λ)** and **(μ + λ)**

The codebase emphasizes clarity, extensibility, and robust documentation.

## Key Features

- **Modular OOP Design:** Core logic is encapsulated in `EvolutionStrategy` and `Individual` classes.
- **Selection Strategies:** Supports both **(μ, λ)** (comma) and **(μ + λ)** (plus) survivor selection.
- **Gaussian Mutation:** Configurable mutation strength (`sigma`) for exploration.
- **Boundary Handling:** Solutions are clipped to remain within user-specified bounds.
- **Benchmark Functions:** Includes the Rastrigin function; easily extensible for others.
- **Visualization:** Generates convergence plots and, for 2D problems, a landscape plot showing the best solution.
- **Logging:** Each run is logged with a unique batch ID, and plots are saved in batch-specific folders.
- **Reproducibility:** Supports random seeds for repeatable experiments.
- **Extensible:** Add new objective functions by editing a single file.

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
├── logs/                           # Output logs directory
├── main.py                         # Main script to run the optimizer
├── plan-to-develop.md              # Future development notes
├── requirements.txt                # Python package dependencies
├── plots/                          # Output plots directory
│   ├── <batch_id>/                 # Run-specific plots
│   └── plots.md                    # Plot documentation/notes
└── report.md                       # Project report
```

[See ES Algorithm Flowchart (diagram.md)](diagram.md)


## Installation

**Requirements:**
- Python 3.8 or newer
- NumPy
- Matplotlib

**Setup:**
1. Clone the repository:
    ```bash
    git clone https://github.com/Romerolweb/COIT29224-EvolutionStrategy.git
    cd COIT29224-EvolutionStrategy
    ```
2. (Recommended) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

Run the main script from the project root:
```bash
python main.py
```
**What happens:**
- The script prints the ES configuration and progress.
- Upon completion, it prints the best solution found.
- Convergence and (if 2D) landscape plots are saved in a batch-specific folder under `plots/`.
- All run details are logged in the `logs/` directory.

## Configuration

Edit the parameters in `main.py` (inside the `run_es_optimization` function or the main block):

- `PROBLEM_DIMENSIONS`: Number of variables (int)
- `SEARCH_BOUNDS`: Tuple of (min, max) for each variable
- `POPULATION_MU`: Number of parents (μ)
- `OFFSPRING_LAMBDA`: Number of offspring (λ)
- `GENERATIONS`: Number of generations
- `MUTATION_SIGMA`: Mutation strength (σ)
- `SELECTION_STRATEGY`: `'(mu, lambda)'` or `'(mu + lambda)'`
- `RANDOM_SEED`: Integer or `None`
- `objective_function`: Function to optimize (e.g., `rastrigin`)

## Adding Objective Functions

1. Define your function in `es_optimiser/objective_functions.py`:
    ```python
    def my_function(x: np.ndarray) -> float:
        # Your implementation
        return value
    ```
2. Update `main.py` to use your function:
    ```python
    from es_optimiser.objective_functions import my_function
    # ...
    es_optimizer = EvolutionStrategy(
        objective_function=my_function,
        # ...
    )
    ```


## Output

- **Logs:** Each run creates a log file in `logs/` with a unique batch ID.
- **Plots:** Convergence and landscape plots are saved in `plots/<batch_id>/`.
- **Console:** Progress and summary statistics are printed.

## License

This project is for academic use. See [LICENSE](./LICENSE).

## Author

- **Sebastian Romero Laguna**
- Orcid:
