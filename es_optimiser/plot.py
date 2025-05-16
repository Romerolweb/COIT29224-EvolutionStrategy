import matplotlib.pyplot as plt
import numpy as np
import os
from typing import List, Tuple, Callable, Optional

from .objective_functions import rastrigin

PLOTS_DIR = "plots"

def ensure_plots_dir():
    """Ensure the plots directory exists."""
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)

def plot_convergence(history: List[Tuple[int, float]], title: Optional[str] = None, filename: Optional[str] = None):
    """
    Generates and saves a plot showing the convergence of the best fitness over generations.

    Args:
        history (List[Tuple[int, float]]): (generation_number, best_fitness_at_that_generation).
        title (Optional[str]): Title for the plot.
        filename (Optional[str]): If provided, saves the plot to this file in the plots directory.
    """
    if not history:
        print("Warning: History is empty, cannot plot convergence.")
        return

    ensure_plots_dir()
    generations = [item[0] for item in history]
    fitnesses = [item[1] for item in history]

    plt.figure(figsize=(10, 6))
    plt.plot(generations, fitnesses, marker='.', linestyle='-', markersize=4)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness Found")
    plot_title = title if title else "ES Convergence History"
    plt.title(plot_title)
    if all(f > 0 for f in fitnesses) and (max(fitnesses) / min(fitnesses) > 100):
        plt.yscale('log')
        plt.ylabel("Best Fitness Found (Log Scale)")
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    if filename:
        plt.savefig(filename)
    plt.close()

def plot_rastrigin_2d_landscape(bounds: Tuple[float, float] = (-5.12, 5.12),
                                best_solution: Optional[np.ndarray] = None,
                                filename: Optional[str] = None):
    """
    Plots and saves the 2D landscape of the Rastrigin function and optionally marks the best solution.

    Args:
        bounds (Tuple[float, float]): The plot range for x1 and x2.
        best_solution (Optional[np.ndarray]): The (x1, x2) coordinates of the best solution found.
        filename (Optional[str]): If provided, saves the plot to this file in the plots directory.
    """
    ensure_plots_dir()
    x = np.linspace(bounds[0], bounds[1], 200)
    y = np.linspace(bounds[0], bounds[1], 200)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = rastrigin(np.array([X[i, j], Y[i, j]]))

    plt.figure(figsize=(10, 8))
    contour = plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar(contour, label='Fitness Value (Rastrigin)')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Rastrigin Function Landscape (2D)')
    plt.axis('equal')
    plt.plot(0, 0, 'ro', markersize=10, markerfacecolor='none', markeredgewidth=2, label='Global Optimum at (0,0)')
    if best_solution is not None and len(best_solution) == 2:
        plt.plot(best_solution[0], best_solution[1], 'y*', markersize=12, markeredgewidth=1.5, label=f'ES Best Solution ({best_solution[0]:.2f}, {best_solution[1]:.2f})')
    plt.legend()
    if filename:
        plt.savefig(filename)
    plt.close()

# Placeholder for future plot types (e.g., overall performance, boxplots, etc.)
def plot_overall_performance(*args, **kwargs):
    """
    Placeholder for future overall performance plots.
    """
    pass