# es_optimiser/objective_functions.py
import numpy as np
from typing import List # Use List for type hinting arrays/sequences if preferred over np.ndarray in some contexts

def rastrigin(x: np.ndarray) -> float:
    """
    Calculates the value of the Rastrigin function for a given input vector.

    The Rastrigin function is a non-convex function commonly used as a performance
    test problem for optimization algorithms. It features a complex landscape with
    numerous local minima and a single global minimum at the origin.

    Formula: f(x) = 10d + Σ[ (xi^2 - 10 * cos(2 * π * xi)) ] for i = 1 to d

    The global minimum is f(0, ..., 0) = 0.

    Args:
        x (np.ndarray): A 1-D numpy array representing the input vector (solution).
                        Each element should be within the function's typical bounds
                        (e.g., [-5.12, 5.12]).

    Returns:
        float: The calculated Rastrigin function value (fitness). Lower is better.

    Example:
        >>> rastrigin(np.array([0.0, 0.0]))
        0.0
        >>> rastrigin(np.array([1.0, 0.0]))
        1.0
    """
    dimension = len(x)
    return 10 * dimension + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

# --- Future development: Add other functions like Ackley and Griewank if desired ---

def ackley(x: np.ndarray) -> float:
    """
    Calculates the value of the Ackley function for a given input vector.

    The Ackley function is a widely used test function for optimization algorithms.
    It has a large number of local minima and a single global minimum at the origin.

    Formula: f(x) = -20 * exp(-0.2 * sqrt(0.5 * Σ[xi^2]) - exp(0.5 * Σ[cos(2 * π * xi)]) + e + 20

    The global minimum is f(0, ..., 0) = 0.

    Args:
        x (np.ndarray): A 1-D numpy array representing the input vector (solution).
                        Each element should be within the function's typical bounds
                        (e.g., [-32.768, 32.768]).

    Returns:
        float: The calculated Ackley function value (fitness). Lower is better.

    Example:
        >>> ackley(np.array([0.0, 0.0]))
        0.0
        >>> ackley(np.array([1.0, 0.0]))
        1.0
    """
    dimension = len(x)
    sum_sq = np.sum(x**2)
    sum_cos = np.sum(np.cos(2 * np.pi * x))
    term1 = -20 * np.exp(-0.2 * np.sqrt(sum_sq / dimension))
    term2 = -np.exp(sum_cos / dimension)
    return term1 + term2 + 20 + np.e

