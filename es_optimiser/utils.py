def print_population(population):
    """Utility function to print the population."""
    for individual, fitness in population:
        print(f"Individual: {individual}, Fitness: {fitness}")