def sphere_function(x):
    """Sphere function: f(x) = sum(x_i^2)"""
    return sum(xi ** 2 for xi in x)

def rastrigin_function(x):
    """Rastrigin function: f(x) = 10n + sum(x_i^2 - 10cos(2πx_i))"""
    import math
    n = len(x)
    return 10 * n + sum(xi ** 2 - 10 * math.cos(2 * math.pi * xi) for xi in x)