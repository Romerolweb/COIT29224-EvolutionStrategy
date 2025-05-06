
# es_optimiser/utils.py
# (Keep plot_convergence, ensure good docstrings/type hints)
# Consider adding the 2D landscape plot function here if needed.
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Callable, Optional

from .objective_functions import rastrigin

def plot_convergence(history: List[Tuple[int, float]], title: Optional[str] = None):
    """
    Generates a plot showing the convergence of the best fitness over generations.

    Args:
        history (List[Tuple[int, float]]): A list where each tuple contains
                                            (generation_number, best_fitness_at_that_generation).
        title (Optional[str], optional): Optional title for the plot.
                                         Defaults to 'ES Convergence History'.
    """
    if not history:
        print("Warning: History is empty, cannot plot convergence.")
        return

    generations = [item[0] for item in history]
    fitnesses = [item[1] for item in history]

    plt.figure(figsize=(10, 6))
    plt.plot(generations, fitnesses, marker='.', linestyle='-', markersize=4)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness Found")
    plot_title = title if title else "ES Convergence History"
    plt.title(plot_title)
    # Use log scale if fitness values span multiple orders of magnitude and are positive
    # Avoid log scale if fitness can be zero or negative, or range is small
    if all(f > 0 for f in fitnesses) and (max(fitnesses) / min(fitnesses) > 100):
         plt.yscale('log')
         plt.ylabel("Best Fitness Found (Log Scale)")

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout() # Adjust layout to prevent labels overlapping
    plt.show()

def plot_rastrigin_2d_landscape(bounds: Tuple[float, float] = (-5.12, 5.12),
                                best_solution: Optional[np.ndarray] = None):
    """
    Plots the 2D landscape of the Rastrigin function and optionally marks the best solution.

    Args:
        bounds (Tuple[float, float], optional): The plot range for x1 and x2.
                                                Defaults to (-5.12, 5.12).
        best_solution (Optional[np.ndarray], optional): The (x1, x2) coordinates of the
                                                        best solution found to mark on the plot.
                                                        Defaults to None.
    """
    x = np.linspace(bounds[0], bounds[1], 200)
    y = np.linspace(bounds[0], bounds[1], 200)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    # Calculate Rastrigin value for each point on the grid
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

    # Mark the global optimum
    plt.plot(0, 0, 'ro', markersize=10, markerfacecolor='none', markeredgewidth=2, label='Global Optimum at (0,0)')

    # Mark the best solution found by ES, if provided
    if best_solution is not None and len(best_solution) == 2:
        plt.plot(best_solution[0], best_solution[1], 'y*', markersize=12, markeredgewidth=1.5, label=f'ES Best Solution ({best_solution[0]:.2f}, {best_solution[1]:.2f})')

    plt.legend()
    plt.show()

